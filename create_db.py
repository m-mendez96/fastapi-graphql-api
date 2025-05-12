import asyncio

from app.db import AsyncSessionLocal, Base, engine
from app.models import Country, TypeDocument


async def create_tables_and_seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        documents = [
            TypeDocument(name_type_document="Cédula de Ciudadanía"),
            TypeDocument(name_type_document="Pasaporte"),
        ]
        session.add_all(documents)

        countries = [
            Country(country_code="CO", country_name="Colombia"),
            Country(country_code="US", country_name="Estados Unidos"),
            Country(country_code="MX", country_name="México"),
            Country(country_code="BR", country_name="Brasil"),
            Country(country_code="AR", country_name="Argentina"),
            Country(country_code="CL", country_name="Chile"),
            Country(country_code="PE", country_name="Perú"),
            Country(country_code="EC", country_name="Ecuador"),
            Country(country_code="VE", country_name="Venezuela"),
            Country(country_code="PA", country_name="Panamá"),
        ]
        session.add_all(countries)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_tables_and_seed())
