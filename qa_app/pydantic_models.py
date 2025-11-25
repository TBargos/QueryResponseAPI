from pydantic import BaseModel, UUID4, Field


class Question(BaseModel):
    text: str = Field(min_length=1)


class Answer(BaseModel):
    text: str = Field(min_length=1)
    uuid: UUID4