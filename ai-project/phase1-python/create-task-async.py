import asyncio


async def long_task():
    print("Long task started")

    await asyncio.sleep(3)

    print("Long task finished")
    return "Long task result"


async def main():

    task = asyncio.create_task(long_task())

    print("Main is doing other work...")

    await asyncio.sleep(1)

    print("Main work finished")

    result = await task

    print(result)


asyncio.run(main())


# 🔥 gather() vs create_task()
# gather()

# Jab multiple operations ke results ek saath chahiye:

# user, orders = await asyncio.gather(
#     get_user(),
#     get_orders()
# )
# create_task()

# Jab task ko abhi schedule karna hai aur baad mein await karna hai:

# task = asyncio.create_task(get_user())

# # do other work

# user = await task