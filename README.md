# FastAPI-GraphQL API

Este es un ejemplo de una API GraphQL basada en FastAPI usando Strawberry.

El ejemplo incluye configuraciones para Docker, y se puede ejecutar con Docker Compose para crear un entorno de desarrollo.

## Requisitos

Para ejecutar el proyecto, se debe tener instalados los siguientes requisitos:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.11 o superior

## Configuración del Proyecto con Docker

1. Clona el repositorio:

   ```bash
   git clone //https:...
   cd fastapi-graphql-api

2. Construir la imágene de Docker y ejecutar el contenedor con Docker Compose:

    ```bash
    docker-compose up --build

3. Una vez que el contenedor estén en funcionamiento, se puede acceder a la aplicación en http://localhost:8080.

## Crear la Base de Datos

1. Crea el entorno virtual con:
   ```bash
   pip install virtualenv

2. Activar el entorno virtual:
   ```bash
   source venv/bin/activate

3. Instalar los requisitos del proyecto:
   ```bash
   pip install -r requirements.txt

4. Inicializar la base de datos, ejecutar el siguiente comando en la terminal:
   ```bash
   python create_db.py

## 🧬 Ejemplo de ejecución de mutación GraphQL

Hacer la solicitud POST al endpoint `/graphql` o desde el navegador a http://127.0.0.1:8080/graphql con el siguiente cuerpo:

```graphql
mutation {
  registerUser(input: {
    lastName: "Mendez"
    name: "Miguel"
    username: "m-mendez96"
    password: "pass123"
    email: "miguel.mendez@example.com"
    document: {
      typeDocumentId: 1
      document: "1122334455"
      placeExpedition: "Bogotá"
      dateExpedition: "2020-01-01"
    }
    contact: {
      address: "Calle 123"
      countryId: 1
      city: "Bogotá"
      phone: "601-123-4567"
      celPhone: "3151234567"
      emergencyName: "Juan"
      emergencyPhone: "3109876543"
    }
  })
}