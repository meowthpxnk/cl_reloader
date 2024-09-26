from cl_getter import get_clickers
from iter_cls import iter_cls

async def analyze(DB_PATH):
    clickers = get_clickers(DB_PATH)
    data = await iter_cls(clickers)

    for res in data:
        if res.get("error"):
            continue
        status = res["req"]["status"]
        if status == 502:
            print(f"{res["device"]["phone"]} Should be reloaded on server {res["device"]["server"]}, port {[res["device"]["port"]]}")
        elif status == 404:
            print(f"Alright with phone {res["device"]["phone"]}")
        else:
            print(f"🤷‍♀️🤷‍♀️🤷‍♀️, Phone {res["device"]["phone"]} statuscode is {status}")


if __name__ == "__main__":
    from get_db_path import get_db_path
    import asyncio
    asyncio.run(analyze(get_db_path()))
