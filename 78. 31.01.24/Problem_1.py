from datetime import datetime
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("price", sqlalchemy.Float)
)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(32))
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("order_date", sqlalchemy.DateTime),
    sqlalchemy.Column("order_status", sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str = Field(max_length=128)
    description: str
    price: float = Field(ge=0)


class InputItem(BaseModel):
    name: str = Field(max_length=128)
    description: str
    price: float = Field(ge=0)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)


class InputUser(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)


class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_date: datetime
    order_status: bool


class InputOrder(BaseModel):
    user_id: int
    item_id: int
    order_date: datetime
    order_status: bool


@app.on_event("startup")
async def startup():
    await database.connect()


@app.post("/items/", response_model=Item)
async def create_item(item: InputItem):
    query = items.insert().values(**item.dict())
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@app.get("/items/", response_model=list[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)


@app.put("/items/{item_id}", response_model=Item)
async def update_user(item_id: int, new_item: InputItem):
    query = items.update().where(items.c.id == item_id).values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": item_id}


@app.delete("/items/{item_id}")
async def delete_user(item_id: int):
    query = users.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}


@app.post("/users/", response_model=User)
async def create_user(user: InputUser):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: InputUser):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.post("/orders/", response_model=Order)
async def create_order(order: InputOrder):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.get("/orders/", response_model=list[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: InputOrder):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
