import aiohttp
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from queue import Queue

BASE_URL = "https://pokeapi.co/api/v2/"


def time_count_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken for processing the API request of {func.__name__}(): {time.time() - start_time}.")
        return result

    return inner


@time_count_decorator
async def get_pokemons(session, type=None):
    if type is None:
        result = await session.get(f"{BASE_URL}/pokemon")
        result_json = await result.json()
        column_names = f"| {'Name:':30} | {'Weight':20} |"
        header_len = len(column_names) - 4
        header = f"| {str('First ' + str(result_json['next'])[-2:] + ' pokemon names and weight.'):{header_len}} | "
        header_separator = "-" * len(column_names)
        print(header_separator)
        print(header)
        print(header_separator)
        print(column_names)
        print(header_separator)
        for i in result_json['results']:
            result = await session.get(i['url'])
            result_json = await result.json()
            print(f"| {str(result_json['name']):30} | {str(result_json['weight']):20} |")
        print(header_separator)
    else:
        result = await session.get(f"{BASE_URL}/type/{type}/")
        result_json = await result.json()
        column_names = f"| {'ID:':5} | {'Name':30} | {'Weight':10} | {'Height':10} |"
        header_len = len(column_names) - 4
        type_name = str(result_json["name"])
        header = f"| {f'Listing the {type_name} pokemons.':{header_len}} | "
        header_separator = "-" * len(column_names)
        print(header_separator)
        print(header)
        print(header_separator)
        print(column_names)
        print(header_separator)
        for i in result_json['pokemon']:
            poke_data = await session.get(i['pokemon']['url'])
            poke_json_data = await poke_data.json()
            # Pretty nice output
            print(f"| {str(poke_json_data['id']):5} | {str(poke_json_data['name']):30} | "
                  f"{str(poke_json_data['weight']):10} | {str(poke_json_data['height']):10} |")
            # Dict output:
            # data = {
            #     'id': poke_json_data['id'],
            #     'name': poke_json_data['name'],
            #     'weight': poke_json_data['weight'],
            #     'height': poke_json_data['height']
            # }
            # print(data)
        print(header_separator)


@time_count_decorator
async def get_pokemon_types(session):
    result = await session.get(f"{BASE_URL}/type/")
    result_json = await result.json()
    poke_count = int(result_json['count'])
    header = f"| {str('Listing of the ' + str(poke_count) + ' pokemon types '):40} |"
    separator_string = "-" * len(header)
    colum_names = f"| {'ID':5} | {'Name':{len(header) - 12}} |"
    print(separator_string)
    print(header)
    print(separator_string)
    print(colum_names)
    print(separator_string)
    for poke_type in result_json['results']:
        poke_id = await session.get(poke_type['url'])
        poke_id_json = await poke_id.json()
        print(f"| {str(poke_id_json['id']):5} | {str(poke_type['name']):32} |")
    print(separator_string)


@time_count_decorator
async def get_pokemons_by_type(session):
    await get_pokemon_types(session)
    type_id = int(input("Please enter the pokemon type ID to print.  "))
    await get_pokemons(session, type_id)

@time_count_decorator
async def main():
    async with aiohttp.ClientSession() as session:
        await get_pokemons(session)
        await get_pokemons_by_type(session)


@time_count_decorator
def get_pokemons_in_threads(session, url_queue):
    with session.get(url_queue.get()) as response:
        print(f" Name: {response.json()['name']} Weight: {response.json()['weight']}")

@time_count_decorator
def form_url_queue(session):
    with session.get(f"{BASE_URL}/pokemon") as response:
        resp_json = response.json()['results']
        url_queue = Queue()
        for r in resp_json:
            url_queue.put(r['url'])
        return url_queue

@time_count_decorator
def main_with_threads():
    with ThreadPoolExecutor(max_workers=20) as executor:
        with requests.Session() as session:
            url_queue = form_url_queue(session)
            executor.map(get_pokemons_in_threads, [session] * 20, [url_queue] * 20)


main_with_threads()

asyncio.run(main())