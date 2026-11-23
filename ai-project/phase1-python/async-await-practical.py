import asyncio


async def get_user():
    print("User started")
    await asyncio.sleep(2)
    print("User completed")


async def get_orders():
    print("Orders started")
    await asyncio.sleep(1)
    print("Orders completed")


async def get_notifications():
    print("Notifications started")
    await asyncio.sleep(1.5)
    print("Notifications completed")


async def main():
    await asyncio.gather(
        get_user(),
        get_orders(),
        get_notifications()
    )


asyncio.run(main())