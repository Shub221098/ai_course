import asyncio


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

# Sequential:
# 2 sec + 1 sec = 3 sec
async def main():
    await task1()
    await task2()

# Concurrent:
# max(2 sec, 1 sec) = 2 sec
async def main2():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

asyncio.run(main2())