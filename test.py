import asyncio


async def test2():
    print(777)


async def test(DB_PATH):
    # clickers = get_clickers(DB_PATH)
    # data = await iter_cls(clickers)

    for res in [1, 2]:
        # if res.get("error"):
        #     print(
        #         f"Error with device {res['device']['phone']} Error: {res.get('error')}"
        #     )
        #     continue
        status = 502
        if status == 502:
            print(
                f"TESTS PASSED"
                # f"{res['device']['phone']} Should be reloaded on server {res['device']['server']}, port {[res['device']['port']]}"
            )

            try:
                await test2()
            except Exception as error:
                print(
                    f"Failed reload device with phone {res['device']['phone']}, Error: {error}"
                )
            continue
        elif status == 404:
            print(f"Alright with phone {res['device']['phone']}")
            continue
        print(
            f"🤷‍♀️🤷‍♀️🤷‍♀️, Phone {res['device']['phone']} statuscode is {status}"
        )


l = asyncio.get_event_loop()

l.run_until_complete(test(123))
