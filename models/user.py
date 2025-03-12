from pydantic import BaseModel

from models.support import SupportData


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    job: str


class UserResponse(BaseModel):
    data: UserData
    support: SupportData


class UserCreateData(BaseModel):
    name: str
    job: str


class UserCreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UserUpdatedResponse(BaseModel):
    name: str
    job: str
    updatedAt: str
