from typing import List

import strawberry
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.types import Info

from app.db import AsyncSessionLocal
from app.graphql.types import (
    AppUserType,
    ContactInfoType,
    CountryType,
    TypeDocumentType,
    UserDocumentType,
)
from app.models import (
    AppUser,
    ContactInfo,
    Country,
    TypeDocument,
    UserDocument,
)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        return session


@strawberry.type
class Query:
    @strawberry.field
    async def type_documents(self, info: Info) -> List[TypeDocumentType]:
        session = await get_session()
        result = await session.execute(select(TypeDocument))
        return [
            TypeDocumentType(
                id=row.id,
                name_type_document=row.name_type_document,
            )
            for row in result.scalars().all()
        ]

    @strawberry.field
    async def countries(self, info: Info) -> List[CountryType]:
        session = await get_session()
        result = await session.execute(select(Country))
        return [
            CountryType(
                id=row.id,
                country_code=row.country_code,
                country_name=row.country_name,
            )
            for row in result.scalars().all()
        ]

    @strawberry.field
    async def app_users(self, info: Info) -> List[AppUserType]:
        session = await get_session()
        result = await session.execute(select(AppUser))
        return [
            AppUserType(
                id=row.id,
                last_name=row.last_name,
                name=row.name,
                is_militar=row.is_militar,
                is_temporal=row.is_temporal,
                time_create=row.time_create,
                username=row.username,
                password=row.password,
                email=row.email,
                email_verified=row.email_verified,
                verification_token=row.verification_token,
            )
            for row in result.scalars().all()
        ]

    @strawberry.field
    async def user_documents(self, info: Info) -> List[UserDocumentType]:
        session = await get_session()
        result = await session.execute(select(UserDocument))
        return [
            UserDocumentType(
                user_id=row.user_id,
                type_document_id=row.type_document_id,
                document=row.document,
                place_expedition=row.place_expedition,
                date_expedition=row.date_expedition,
            )
            for row in result.scalars().all()
        ]

    @strawberry.field
    async def contact_infos(self, info: Info) -> List[ContactInfoType]:
        session = await get_session()
        result = await session.execute(select(ContactInfo))
        return [
            ContactInfoType(
                id=row.id,
                user_id=row.user_id,
                address=row.address,
                country_id=row.country_id,
                city=row.city,
                phone=row.phone,
                cel_phone=row.cel_phone,
                emergency_name=row.emergency_name,
                emergency_phone=row.emergency_phone,
            )
            for row in result.scalars().all()
        ]
