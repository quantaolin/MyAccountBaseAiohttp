# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Account(Base):
    __tablename__ = 'account'

    ID = Column(Integer, primary_key=True)
    ACCOUNT_ID = Column(String(45), nullable=False, unique=True)
    ACCOUNT_TYPE = Column(String(45), nullable=False)
    USER_ID = Column(String(45), nullable=False)
    BALANCE = Column(Numeric(10, 0), nullable=False)
    
a = Account()
a.metadata.insert().values()

class Order(Base):
    __tablename__ = 'order'

    ID = Column(Integer, primary_key=True)
    ORDER_ID = Column(String(45), nullable=False, unique=True)
    ORDER_TYPE = Column(String(45), nullable=False)
    FROM_USER_ID = Column(String(45), nullable=False)
    AMOUNT = Column(Numeric(10, 0), nullable=False)
    TO_USER_ID = Column(String(45), nullable=False)



class User(Base):
    __tablename__ = 'user'

    ID = Column(Integer, primary_key=True)
    USER_ID = Column(String(45), nullable=False, unique=True)
    USER_NAME = Column(String(45), nullable=False)
    SEX = Column(String(2), nullable=False)
    CARD_NUM = Column(String(45), nullable=False)
