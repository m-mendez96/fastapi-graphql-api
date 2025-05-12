import strawberry
from passlib.hash import bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.db import AsyncSessionLocal
from app.graphql.inputs import RegisterUserInput
from app.models import AppUser, ContactInfo, UserDocument


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def register_user(self, input: RegisterUserInput) -> str:
        async with AsyncSessionLocal() as session:
            query = await session.execute(
                select(AppUser).where(
                    (AppUser.email == input.email)
                    | (AppUser.username == input.username)
                )
            )
            if query.scalar():
                return "Usuario o correo ya registrado."

            hashed_password = bcrypt.hash(input.password)

            user = AppUser(
                name=input.name,
                last_name=input.last_name,
                username=input.username,
                password=hashed_password,
                email=input.email,
            )
            session.add(user)
            await session.flush()

            document = UserDocument(
                user_id=user.id,
                type_document_id=input.document.type_document_id,
                document=input.document.document,
                place_expedition=input.document.place_expedition,
                date_expedition=input.document.date_expedition,
            )
            session.add(document)

            contact = ContactInfo(
                user_id=user.id,
                address=input.contact.address,
                country_id=input.contact.country_id,
                city=input.contact.city,
                phone=input.contact.phone,
                cel_phone=input.contact.cel_phone,
                emergency_name=input.contact.emergency_name,
                emergency_phone=input.contact.emergency_phone,
            )
            session.add(contact)

            try:
                await session.commit()
                return "Usuario registrado exitosamente."
            except IntegrityError:
                await session.rollback()
                return (
                    "Error al registrar: posible duplicado o datos inválidos."
                )
