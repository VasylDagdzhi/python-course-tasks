import aiohttp
import asyncio
import time

BASE_URL = "https://pokeapi.co/api/v2/"


async def get_pokemons(session):
    result = await session.get(BASE_URL)
    result_json= await result.json()
    print(result_json)


async def main():
    async with aiohttp.ClientSession() as session:
        await get_pokemons(session)


asyncio.run(main())
