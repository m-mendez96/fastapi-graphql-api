from datetime import date

import strawberry


@strawberry.input
class DocumentInput:
    type_document_id: int
    document: str
    place_expedition: str
    date_expedition: date


@strawberry.input
class ContactInput:
    address: str
    country_id: int
    city: str
    phone: str
    cel_phone: str
    emergency_name: str
    emergency_phone: str


@strawberry.input
class RegisterUserInput:
    last_name: str
    name: str
    username: str
    password: str
    email: str
    document: DocumentInput
    contact: ContactInput
