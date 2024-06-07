from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CategoryCars(Base):
    __tablename__ = "category_cars"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, unique=True, nullable=False)

    cars = relationship("Cars", back_populates="category")


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('category_cars.id'))

    category = relationship("CategoryCars", back_populates="cars")
