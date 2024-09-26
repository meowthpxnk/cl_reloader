import aiohttp

URL = "http://127.0.0.1:5000/api/device"


async def reload_device(phone):
    async with aiohttp.ClientSession() as session:
        print(f"Start reload device with phone {phone}")
        await session.put(f"{URL}/stop", json={"phone": phone})
        print(f"Device stopped successfull {phone}")
        await session.put(f"{URL}/start", json={"phone": phone})
        print(f"Device started successfull {phone}")


if __name__ == "__main__":
    import asyncio
    from get_db_path import get_db_path

    loop = asyncio.get_event_loop()
    loop.run_until_complete(reload_device(get_db_path()))
