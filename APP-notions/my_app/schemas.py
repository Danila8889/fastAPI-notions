from pydantic import BaseModel


class NotionSchema(BaseModel):
    network: str

class ReadNotion(NotionSchema):
    id: int

class CreateNotion(NotionSchema):
    pass