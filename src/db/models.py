from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, relationship, Mapped



Base = declarative_base()


class Geo(Base):
    __tablename__ = 'geo'

    id: Mapped[int] = mapped_column(primary_key=True)
    lat: Mapped[str] = mapped_column()
    lng: Mapped[str] = mapped_column()

    address_id: Mapped[int] = mapped_column(ForeignKey('address.id', ondelete='CASCADE'))
    address: Mapped["Address"] = relationship("Address", back_populates="geo")


class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column()
    suite: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    zipcode: Mapped[str] = mapped_column()

    geo: Mapped["Geo"] = relationship("Geo", uselist=False, back_populates="address")

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped["User"] = relationship("User", back_populates="address")


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    catch_phrase: Mapped[str] = mapped_column()
    bs: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped["User"] = relationship("User", back_populates="company")


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    website: Mapped[str] = mapped_column()

    address: Mapped["Address"] = relationship("Address", uselist=False, back_populates="user")
    company: Mapped["Company"] = relationship("Company", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
