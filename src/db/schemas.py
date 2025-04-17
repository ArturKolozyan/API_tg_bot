from pydantic import BaseModel, Field


class GeoSchema(BaseModel):
    lat: str
    lng: str


class AddressSchema(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoSchema


class CompanySchema(BaseModel):
    name: str
    catch_phrase: str = Field(alias='catchPhrase')
    bs: str


class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: AddressSchema
    phone: str
    website: str
    company: CompanySchema
