import json
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from src.models.models import Quest, Character
from src.models.serializers import QuestResponse
from src.config.open_ai_model import openai_client
from src.utils.prompt import create_quest_prompt, prompt_maps
from src.utils.exceptions import DeadOrWinner, LastQuestNotFinished


async def create_quest_handler(current_character: Character, db: Session):
    try:
        # future make this a dependency
        if current_character.char_state in ('dead', 'winner'):
            raise DeadOrWinner(
                """Can't play anymore. Your character's either dead or yourjourney came
              to an end after exploring the whole world and coming victorious."""
            )
        # future make this a dependency or middleware
        if current_character.quests:
            last_quest: Quest = (current_character.quests
                                 .options(joinedload(Quest.character))
                                 .order_by(desc(Quest.created_at))
                                 .first())

            if last_quest and last_quest.selected_approach is None:
                raise LastQuestNotFinished(
                    f"""Can't create quest. Please finish your last one called '{
                        last_quest.title}' """
                )

        quest_map = prompt_maps[current_character.map_level]

        system_prompt, user_prompt = create_quest_prompt(current_character.username,
                                                         current_character.class_,
                                                         quest_map,
                                                         current_character.virtue,
                                                         current_character.flaw)
        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=1.0
        )
        result = json.loads(completion.choices[0].message.content)

        # Cost calc
        usage_tokens = completion.usage
        cost = (usage_tokens.prompt_tokens * 0.00001) + \
            (usage_tokens.completion_tokens * 0.00003)

        quest = Quest(
            title=result['title'],
            description=result['description'],
            character_username=current_character.username,
            approaches=result['approaches'],
            cost=cost
        )
        db.add(quest)
        db.commit()

        # serialize response to not expose game secret data
        response = QuestResponse.model_validate(quest, from_attributes=True)
        serialized_quest = response.model_dump()
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content={"quest": serialized_quest})

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


async def get_self_quests_handler(current_character_username: str, db: Session):
    try:
        quests = db.query(Quest).filter(
            Quest.character_username == current_character_username).all()
        if not quests:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"{current_character_username} didn't generate any quest yet.")

        # If quest hasn't been completed, hide quest success chance, and choices descriptions.
        serialized_quests = []
        for quest in quests:
            if quest.selected_approach is None:
                quest = QuestResponse.model_validate(
                    quest, from_attributes=True)
                quest = quest.model_dump()
                serialized_quests.append(quest)
            else:
                serialized_quests.append(quest)
        return serialized_quests
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


async def get_quest_handler(quest_id: int, db: Session):
    try:
        quest: Quest = db.query(Quest).filter(
            Quest.quest_id == quest_id).first()

        if not quest:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Quest doesn't exist")
        # If quest hasn't been completed, hide quest success chance, and choices descriptions.
        if quest.selected_approach is None:
            quest = QuestResponse.model_validate(quest, from_attributes=True)
            return quest.model_dump()
        return quest
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


async def get_character_quests_handler(character_username: str, db: Session):
    try:
        quests = db.query(Quest).filter(
            Quest.character_username == character_username).all()
        if not quests:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"{character_username} didn't generate any quest yet.")

        # If quest hasn't been completed, hide quest success chance, and choices descriptions.
        serialized_quests = []
        for quest in quests:
            if quest.selected_approach is None:
                quest = QuestResponse.model_validate(
                    quest, from_attributes=True)
                quest = quest.model_dump()
                serialized_quests.append(quest)
            else:
                serialized_quests.append(quest)
        return serialized_quests
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
