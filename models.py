from . import peach
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, ForeignKey, DateTime, DECIMAL, Numeric, List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

import datetime
import decimal
import uuid
import enum



db = SQLAlchemy(peach)

class Base(DeclarativeBase):
    pass

class TransferSources(enum.Enum):
    WALLET  = "Wallet"
    ACCOUNT = "Account"


class AccountType(enum.Enum):
    CURRENT_ACCOUNT  = "Bank"
    SAVINGS = "Savings"
    SINKING_FUNDS = "Sinking Funds"

class WalletType(enum.Enum):
    MOBILE_MONEY = "Mobile Money"
    CASH = "Cash"



class Category(db.Model):
    """
    A category represents a type of expense frequently used
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    expenses = Mapped[List["Expense"]], relationship("Expense", back_populates="category")



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



# class Transfers(db.Model):
#     """
#     A transfer represents a movement of funds to and from accounts and wallets
#     """
#     __tablename__ = "transfers"

#     source = Mapped[str] = mapped_column(TransferSources, nullable=False)
#     destination =  Mapped[str] = mapped_column(TransferSources, nullable=False)
#     intent = Mapped[str] = mapped_column(String(150),nullable=False)
#     transaction_cost = Mapped[int] = mapped_column(Numeric, nullable=False)

# class Account():
#     """
#     An account is a place where money is kept. It could be current, savings, sinking funds typically associated with some sort of financial/budgeting goal
#     """
#     __tablename__ = "accounts"

#     name: Mapped[str] = mapped_column(String(50),nullable=False)
#     account_number: Mapped[int] = mapped_column(Integer,nullable=True)
#     account_balance: Mapped[int] = mapped_column(Numeric, nullable=False)


# class Wallet():
#     """
#     A wallet is sort of a holding place before payments are made.
#     """
#     __tablename__ = "wallets"

#     wallet_name: Mapped[str] = mapped_column(String(80))
#     wallet_balance: Mapped[int] = mapped_column(Numeric, nullable=False) 

