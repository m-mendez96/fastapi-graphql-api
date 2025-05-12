import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.graphql.mutation import Mutation
from app.graphql.query import Query

app = FastAPI()

schema = strawberry.federation.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root():
    return {"message": "FastAPI-GraphQL-API."}
