from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from wtforms.validators import DataRequired, URL, Email, Length
from sqlalchemy import Integer, String, Text
from flask_login import UserMixin
from sqlalchemy import DateTime, func

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Good(db.Model):
    __tablename__ = "goods"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String, nullable=False)
    size: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    made_of: Mapped[str] = mapped_column(Text, nullable=False)
    addedAt: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now())
