import aiohttp

from root_servers import root_servers


async def req(port, server, phone):
    async with aiohttp.ClientSession() as session:
        r = await session.get(f"http://{root_servers[server]}/{port}/outbox")
        status = r.status
        text = await r.text()

        try:
            data = await r.json()
        except:
            data = None
        return data, status, text
