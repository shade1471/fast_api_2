from pydantic import BaseModel


class SupportData(BaseModel):
    url: str
    text: str
