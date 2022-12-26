import aiohttp
import asyncio
import time

BASE_URL = "https://pokeapi.co/api/v2/"


async def get_pokemons(session):
    start_time = time.time()
    result = await session.get(f"{BASE_URL}/pokemon")
    result_json = await result.json()
    # print(result_json)
    header = f"| {'Pokemon name:':30} | {'Pokemon weight':20} |"
    header_separator = "-"*len(header)
    print(header_separator)
    print(header)
    print(header_separator)
    for i in result_json['results']:
        result = await session.get(i['url'])
        result_json = await result.json()
        print(f"| {str(result_json['name']):30} | {str(result_json['weight']):20} |")
    print(header_separator)
    print(f"Time taken for processing the API requests: {time.time()-start_time}.")


async def main():
    async with aiohttp.ClientSession() as session:
        await get_pokemons(session)


asyncio.run(main())
