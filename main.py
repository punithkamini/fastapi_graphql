from fastapi import FastAPI
from db_connections import metadata, engine, conn, tables
from strawberry.fastapi import GraphQLRouter
import strawberry
from schemas import CreateItem, UpdateItem
from typing import List

from sqlalchemy import select, update, delete

metadata.create_all(bind=engine)

app = FastAPI()


@strawberry.type
class Query:
    @strawberry.field
    def get_items(self) -> List[str]:
        res = select(tables['items'])
        return [str(dict(row)) for row in conn.execute(res)]

    @strawberry.field
    def get_item(self, itemId: int) -> List[str]:
        res = (select(tables["items"]).where(tables["items"].c["itemId"] == itemId))
        return [str(dict(row)) for row in conn.execute(res)]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_item(self, item: CreateItem) -> str:
        values = {"itemId": item.itemId, "itemName": item.itemName, "description":item.description,
                  "price": item.price}
        new_item = tables["items"].insert().values(values)
        conn.execute(new_item)
        return f"Created new item with itemId {item.itemId}"

    @strawberry.mutation
    def update_item(self, itemId: int, item:UpdateItem) -> str:
        values={tables["items"].c["itemName"]: item.itemName, tables["items"].c["description"]: item.description,
                tables["items"].c["price"]: item.price}
        res = update(tables["items"]).where(tables["items"].c["itemId"] == itemId).values(values)
        conn.execute(res)
        return f"Updated item with itemId {itemId}"

    @strawberry.mutation
    def delete_item(self, itemId: int) -> str:
        res=delete(tables["items"]).where(tables["items"].c["itemId"]==itemId)
        conn.execute(res)
        return f"Deleted item with itemId {itemId}"


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql = GraphQLRouter(schema)
app.include_router(graphql, prefix='/graphql')
