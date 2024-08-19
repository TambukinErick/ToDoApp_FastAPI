import datetime
from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr
    registered_at: datetime.datetime
    disabled: bool = Field(default=False)

class UserOutput(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    registered_at: datetime.datetime

class UpdateUser(BaseModel):
    user_id: int
    username: str
    email: EmailStr

class SystemUser(BaseModel):
    user_id: int
    email: str
    password: str

class DeleteUser(BaseModel):
    email: str
    password: str