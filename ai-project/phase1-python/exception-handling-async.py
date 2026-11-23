import asyncio


async def get_user():
    await asyncio.sleep(1)
    return "User Data"


async def get_orders():
    await asyncio.sleep(2)
    raise Exception("Database connection failed")


async def get_notifications():
    await asyncio.sleep(1.5)
    return "Notifications Data"


async def main():

    try:
        # It will raise an exception and stop execution of the other tasks
        # user, orders, notifications = await asyncio.gather(
        #     get_user(),
        #     get_orders(),
        #     get_notifications()
        # )

        # It will handle the exception and continue execution of the other tasks
        user, orders, notifications = await asyncio.gather(
            get_user(),
            get_orders(),
            get_notifications(),
            return_exceptions=True
        )

        print(user)
        print(orders)
        print(notifications)

    except Exception as e:
        print("Error:", e)


asyncio.run(main())