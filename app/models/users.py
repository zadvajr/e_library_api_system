from pydantic import BaseModel, EmailStr

class Users(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

