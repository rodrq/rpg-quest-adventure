from sqlalchemy.orm import Session
from src.models.models import Quest
from src.models.schemas import CharacterGameData
from src.models.serializers import QuestResponse
from src.config.open_ai_model import openai_client
import json
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from src.utils.prompt import create_quest_prompt, prompt_maps
from src.utils.exceptions import DeadOrWinner


async def create_quest_handler(current_character_game_data: CharacterGameData, db: Session):
  try:
    #TODO make this a dependency
    if current_character_game_data.char_state == 'dead' or current_character_game_data.char_state == 'winner':
      raise DeadOrWinner(
              """Can't play anymore. Your character's either dead or yourjourney came
              to an end after exploring the whole world and coming victorious."""
              )
    
    quest_map = prompt_maps[current_character_game_data.map_level]
    
    system_prompt, user_prompt = create_quest_prompt(current_character_game_data.username,
                                                     current_character_game_data.class_,
                                                     quest_map, 
                                                     current_character_game_data.virtue, 
                                                     current_character_game_data.flaw)
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={ "type": "json_object" },
        temperature=1.0
    )
    result = json.loads(completion.choices[0].message.content)
    usage_tokens = completion.usage
    cost = (usage_tokens.prompt_tokens * 0.00001) + (usage_tokens.completion_tokens * 0.00003)
    
    quest = Quest(
        title=result['title'],
        description=result['description'],
        character_username=current_character_game_data.username,
        approaches=result['approaches'],
        cost = cost
    ) 
    db.add(quest)
    db.commit()
    return JSONResponse(content={"quest": result})
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

async def get_self_quests_handler(current_character_username: str, db: Session):
  try:
    quests = db.query(Quest).filter(Quest.character_username == current_character_username).all()
    #If quest hasn't been completed, hide quest success chance, and choices descriptions. 
    serialized_quests = []
    for quest in quests:
      if quest.selected_approach == None:
          quest = QuestResponse.model_validate(quest, from_attributes=True)
          quest = quest.model_dump()
          serialized_quests.append(quest)
      else:
        serialized_quests.append(quest)
    return serialized_quests
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

async def get_quest_handler(quest_id: int, db: Session):
    try:
        quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
        if not quest:
          raise HTTPException(status_code=401, detail="Quest doesn't exist.")
        
        #If quest hasn't been completed, hide quest success chance, and choices descriptions. 
        if quest.selected_approach == None:
          quest = QuestResponse.model_validate(quest, from_attributes=True)
          return quest.model_dump()
        return quest
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_character_quests_handler(character_username: str, db: Session):
  try:
    quests = db.query(Quest).filter(Quest.character_username == character_username).all()
    if not quests:
        raise HTTPException(status_code=404, detail= f"{character_username} didn't generate any quest yet.")
      
    #If quest hasn't been completed, hide quest success chance, and choices descriptions. 
    serialized_quests = []
    for quest in quests:
      if quest.selected_approach == None:
          quest = QuestResponse.model_validate(quest, from_attributes=True)
          quest = quest.model_dump()
          serialized_quests.append(quest)
      else:
        serialized_quests.append(quest)
    return serialized_quests
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
  