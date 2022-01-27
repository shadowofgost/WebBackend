from pydantic import BaseModel


class Token(BaseModel):
    access_token : str
    token_type :str


class UserCreate(BaseModel):
    id : str
    password : str

class UserInDB(BaseModel):
    id : str

class User(UserInDB):
    id : str
    password : str

    class Config:
        orm_mode = True