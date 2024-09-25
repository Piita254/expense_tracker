from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    expenses = relationship('Expense', back_populates='user')

    def __repr__(self):
        return f"User(name={self.name})"


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    expenses = relationship('Expense', back_populates='category')

    def __repr__(self):
        return f"Category(name={self.name})"


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    user = relationship('User', back_populates='expenses')
    category = relationship('Category', back_populates='expenses')

    def __repr__(self):
        return f"Expense(description={self.description}, amount={self.amount}, user_id={self.user_id}, category_id={self.category_id})"
