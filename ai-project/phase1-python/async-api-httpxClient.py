import asyncio
import httpx


async def get_post():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        print(response.status_code)
        print(response.json())


asyncio.run(get_post())