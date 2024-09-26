import asyncio


async def test2():
    print("test case 777")


async def test():
    try:
        await test2()
    except:
        print("failed")


l = asyncio.get_event_loop()

l.run_until_complete(test())
