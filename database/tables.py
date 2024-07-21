from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
# from flask_sqlalchemy.model import Model
# from app import db
# from __init__ import db
from database.model import db


class User(db.Model):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    writings: Mapped[List["Writing"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(db.Model):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

class Writing(db.Model):
    __tablename__ = "writing"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    topic: Mapped[str]
    keywords: Mapped[str]
    characters: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="writings")
    def __repr__(self) -> str:
        return f"Writing(id={self.id!r}, topic={self.topic!r})"

# tables = tuple((x for x in locals() if type(x) == SQLAlchemy.model.Model))
# for x in locals():
#     if type(x) == SQLAlchemy.model.Model:
#         print("table:",x)