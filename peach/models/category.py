from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime, DECIMAL, Numeric
from peach.extensions import db 
from typing import List, Optional
import datetime
from sqlalchemy.sql import func




class Category(db.Model): # type: ignore
    """
    A category represents a type of expense frequently used
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class Expense(db.Model):# type: ignore
    """
    An expense is an amount of money spent on a specific item 
    """

    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[int] = mapped_column(Numeric, nullable=False)
    payee: Mapped[str] = mapped_column(String(50),nullable=False)
    item: Mapped[str] = mapped_column(String(50),nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    notes: Mapped[str] =  mapped_column(String(150),nullable=True)
    category_name = mapped_column(ForeignKey("category.name"))