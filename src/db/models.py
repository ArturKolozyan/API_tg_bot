from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Geo(Base):
    __tablename__ = 'geo'

    id: Mapped[int] = mapped_column(primary_key=True)
    lat: Mapped[str]
    lng: Mapped[str]

    address_id: Mapped[int] = mapped_column(ForeignKey('address.id', ondelete='CASCADE'))
    address: Mapped["Address"] = relationship("Address", back_populates="geo")


class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str]
    suite: Mapped[str]
    city: Mapped[str]
    zipcode: Mapped[str]

    geo: Mapped["Geo"] = relationship("Geo", uselist=False, back_populates="address")

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped["User"] = relationship("User", back_populates="address")


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    catch_phrase: Mapped[str]
    bs: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped["User"] = relationship("User", back_populates="company")


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    website: Mapped[str]

    address: Mapped["Address"] = relationship("Address", uselist=False, back_populates="user")
    company: Mapped["Company"] = relationship("Company", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
