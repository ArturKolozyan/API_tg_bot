from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Geo(Base):
    __tablename__ = 'geo'

    id: int = mapped_column(primary_key=True)
    lat: str = mapped_column()
    lng: str = mapped_column()

    address_id: int = mapped_column(ForeignKey('address.id'))
    address = relationship("Address", back_populates="geo")


class Address(Base):
    __tablename__ = 'address'

    id: int = mapped_column(primary_key=True)
    street: str = mapped_column()
    suite: str = mapped_column()
    city: str = mapped_column()
    zipcode: str = mapped_column()

    geo = relationship("Geo", uselist=False, back_populates="address")

    user_id: int = mapped_column(ForeignKey('users.id'))
    user = relationship("User", back_populates="address")


class Company(Base):
    __tablename__ = 'company'

    id: int = mapped_column(primary_key=True)
    name: str = mapped_column()
    catch_phrase: str = mapped_column()
    bs: str = mapped_column()

    user_id: int = mapped_column(ForeignKey('users.id'))
    user = relationship("User", back_populates="company")


class User(Base):
    __tablename__ = 'users'

    id: int = mapped_column(primary_key=True)
    name: str = mapped_column()
    username: str = mapped_column()
    email: str = mapped_column()
    phone: str = mapped_column()
    website: str = mapped_column()
    address: str = relationship("Address", uselist=False, back_populates="user")
    company: str = relationship("Company", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
