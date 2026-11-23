import asyncio
from fastapi import FastAPI

app = FastAPI()


async def get_user():
    await asyncio.sleep(2)
    return {
        "id": 101,
        "name": "Shubham"
    }


async def get_orders():
    await asyncio.sleep(1)
    return [
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 1000}
    ]


@app.get("/dashboard")
async def dashboard():

    user, orders = await asyncio.gather(
        get_user(),
        get_orders()
    )

    return {
        "user": user,
        "orders": orders
    }