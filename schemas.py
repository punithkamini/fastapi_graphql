import strawberry


@strawberry.type
class Item:
    itemId: int
    itemName: str
    description: str
    price: int


@strawberry.input
class CreateItem:
    itemId: int
    itemName: str
    description: str
    price: int


@strawberry.input
class UpdateItem:
    itemName: str
    description: str
    price: int