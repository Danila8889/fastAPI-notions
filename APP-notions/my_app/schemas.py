from pydantic import BaseModel


class ReadNotion(BaseModel):
    id: int
    network: str


class CreateNotion(BaseModel):
    network: str


class UpdateNotion(BaseModel):
    network: str | None
