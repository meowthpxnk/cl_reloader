import asyncio


async def test():
    print("test case 777")


l = asyncio.get_event_loop()

l.run_until_complete(test())
