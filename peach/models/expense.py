
from .. import peach
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, ForeignKey, DateTime, DECIMAL, Numeric, List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .models import Category
from app.extensions import db

import datetime
import decimal
import uuid
import enum

db = SQLAlchemy(peach)


class Expense(db.Model):
    """
    An expense is an amount of money spent on a specific item 
    """

    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[int] = mapped_column(Numeric, nullable=False)
    payee: Mapped[str] = mapped_column(String(50),nullable=False)
    category: Mapped["Category"] = relationship("Category", back_populates="category_name")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    notes: Mapped[str] =  mapped_column(String(150),nullable=True)