import asyncio


async def test2():
    print("test case 777")


async def test():
    await test2()


l = asyncio.get_event_loop()

l.run_until_complete(test())
