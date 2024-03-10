# from typing import Optional
# from pydantic import BaseModel, ConfigDict

# class ApproachGameResponse(BaseModel):
#     choice_description: str


# class NestedApproaches(BaseModel):
#     approach_1: ApproachGameResponse
#     approach_2: ApproachGameResponse
#     approach_3: ApproachGameResponse


# class QuestResponse(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#     quest_id: int
#     title: str
#     description: str
#     character_username: str
#     approaches: NestedApproaches
#     selected_approach: Optional[int]


# class Approach(BaseModel):
#     choice_description: str
#     success_description: str
#     failure_description: str
#     chance_of_success: int
