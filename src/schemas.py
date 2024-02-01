from datetime import date
from typing import List, Optional
from pydantic import *


class ContactBase(BaseModel):
    firstname: str = Field(max_length=25)
    lastname: str = Field(max_length=25)
    email: EmailStr = Field(max_length=100)
    phone: int = Field()


class ContactModel(ContactBase):
    birthday: date = Field(None, description="The birthday date Day-Month-Year")


class ContactUpdate(ContactModel):  # updates the whole contact
    done: bool


class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
