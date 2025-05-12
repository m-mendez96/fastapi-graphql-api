from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

import strawberry


@dataclass
@strawberry.type
class TypeDocumentType:
    id: int
    name_type_document: str


@dataclass
@strawberry.type
class CountryType:
    id: int
    country_code: str
    country_name: str


@dataclass
@strawberry.type
class ContactInfoType:
    id: int
    user_id: int
    address: str
    country_id: int
    city: str
    phone: str
    cel_phone: str
    emergency_name: str
    emergency_phone: str


@dataclass
@strawberry.type
class UserDocumentType:
    user_id: int
    type_document_id: int
    document: str
    place_expedition: str
    date_expedition: date


@dataclass
@strawberry.type
class AppUserType:
    id: int
    last_name: str
    name: str
    is_militar: bool
    is_temporal: bool
    time_create: datetime
    username: str
    password: str
    email: str
    email_verified: bool
    verification_token: Optional[str]
