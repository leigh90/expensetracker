from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime, DECIMAL, Numeric
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from peach.extensions import db 
from typing import List, Optional
import datetime
from sqlalchemy.sql import func
import enum


class TransferSources(str, enum.Enum):
    WALLET  = "Wallet"
    ACCOUNT = "Account"


class AccountType(enum.Enum):
    CURRENT_ACCOUNT  = "Bank"
    SAVINGS = "Savings"
    SINKING_FUNDS = "Sinking Funds"
    WALLET = "Wallet"
    EXPENSE = "Expense"

class WalletType(enum.Enum):
    MOBILE_MONEY = "Mobile Money"
    CASH = "Cash"

TransferSourcesType: pgEnum = pgEnum(
    TransferSources,
    name="transfersource",
    create_constraint=True,
    validate_strings=True,
)

AccountTransactionType: pgEnum = pgEnum(
    AccountType, 
    name = "accounttype",
    validate_strings=True,
)


class TransactionType(str, enum.Enum):
    INCOME  = "Income"
    EXPENSE = "Expense"

TransactionTypes: pgEnum = pgEnum(
    TransactionType,
    validate_strings=True,
)


# class Transaction(db.Model):
#     """
#     Represents a movement of money from one entity to another
#     """
#     __tablename__ = "transactions"

#     id: Mapped[int] = mapped_column(Integer,primary_key=True)
#     source: Mapped[AccountType]
#     destination:  Mapped[AccountType]
#     transaction_type: Mapped[TransactionType]
#     created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
#     notes: Mapped[str] =  mapped_column(String(150),nullable=False)
#     amount: Mapped[int] = mapped_column(Numeric, nullable=False)
#     transaction_cost: Mapped[int] = mapped_column(Numeric, nullable=False) 
#     # user = mapped_column(ForeignKey("user.id"))

# class Transaction(db.Model):
#     """
#     Represents a movement of money from one entity to another
#     """
#     __tablename__ = "transactions"

#     id: Mapped[int] = mapped_column(Integer,primary_key=True)
#     source: Mapped[AccountType]
#     destination:  Mapped[AccountType]
#     # transaction_type: Mapped[TransactionType]
#     created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
#     # notes: Mapped[str] =  mapped_column(String(150),nullable=False)
#     amount: Mapped[int] = mapped_column(Numeric, nullable=False)
#     transaction_cost: Mapped[int] = mapped_column(Numeric, nullable=False) 
    # user = mapped_column(ForeignKey("user.id"))   
    
class Category(db.Model): # type: ignore
    """
    A category represents a type of expense frequently used
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

# class Expense(Transaction):# type: ignore
#     """
#     An expense is an amount of money spent on a specific item 
#     """

#     __tablename__ = "expenses"

#     id: Mapped[int] = mapped_column(Integer,primary_key=True)
#     category_name = mapped_column(ForeignKey("category.name"))
#     transaction_id = mapped_column(ForeignKey("transactions.id"))
    


class User(db.Model):
    __tablename__="users"
    
    """
    A user represents an entity that can create expenses and own accounts
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    # expenses = mapped_column()
    # wallet = mapped_column(ForeignKey("wallet.wallet_id"))
    # accounts = mapped_column(ForeignKey("account.account_id"))


class Account(db.Model):
    """
    An account is a place where money is kept. It could be current, savings, sinking funds typically associated with some sort of financial/budgeting goal
    """
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    type: Mapped[AccountType]
    identification_number: Mapped[str] = mapped_column(String(120),nullable=False)
    balance: Mapped[int] = mapped_column(Numeric, nullable=False)
    # user = mapped_column(ForeignKey("user.id"))

# class Wallet(Account):
#     """
#     Mobile money wallet 
#     """
#     __tablename__ = "wallets"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     phone_number: Mapped[str] = mapped_column(String, nullable=False)
#     account_id = mapped_column(ForeignKey("accounts.id"))


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
    user = mapped_column(ForeignKey("users.id"))


class Transfers(db.Model):
    """
    A transfer represents a movement of funds to and from accounts and wallets
    """
    __tablename__ = "transfers"

    transfer_reference_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source: Mapped[TransferSources]
    destination:  Mapped[TransferSources]
    intent: Mapped[str] = mapped_column(String(150),nullable=False)
    transaction_cost: Mapped[int] = mapped_column(Numeric, nullable=False) 
    user = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


# class Wallet(Account):
#     """
#     A wallet is sort of a holding place before payments are made.
#     """
#     __tablename__ = "wallets"

#     # wallet_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     # wallet_name: Mapped[str] = mapped_column(String(80))
#     # wallet_balance: Mapped[int] = mapped_column(Numeric, nullable=False) 
#     # user = mapped_column(ForeignKey("user.id"))


