from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import *
from datetime import datetime, timedelta


# Show all contacts
async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(
        firstname=body.firstname,
        lastname=body.lastname,
        email=body.email,
        phone=body.phone,
        birthday=body.birthday,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(
    contact_id: int, body: ContactUpdate, db: Session
) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.firstname = (body.firstname,)
        contact.lastname = (body.lastname,)
        contact.email = (body.email,)
        contact.phone = (body.phone,)
        contact.birthday = (body.birthday,)
        contact.done = body.done
        db.commit()
    return contact


async def get_birthdays(db: Session) -> Contact | None:
    seven_days_birth = datetime.now().date() + timedelta(days=7)
    contacts = db.query(Contact).filter(Contact.birthday == seven_days_birth).all()
    return contacts


async def get_search_contacts(search_word, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(
        Contact.firstname.ilike(search_word)
        | Contact.lastname.ilike(search_word)
        | Contact.email.ilike(search_word)
    )
    return contact
