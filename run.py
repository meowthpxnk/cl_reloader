# # from req import req
from iter_cls import iter_cls
from cl_getter import get_clickers

# import asyncio

# import json

# clickers = get_clickers("new_connector.db")
# data = asyncio.run(iter_cls(clickers))

# with open("analysis.json", "w") as f:
#     f.write(json.dumps(data, indent=4))


import asyncio
from get_db_path import get_db_path

loop = asyncio.new_event_loop()

SLEEP_TIME = 300
from analyze import analyze


async def task_schedule():
    db_path = get_db_path()
    while True:
        print("Start analyze clickers")
        await analyze(db_path)
        print("End analyze clickers")
        print(f"Need to sleep {SLEEP_TIME} seconds.")
        await asyncio.sleep(SLEEP_TIME)


if __name__ == "__main__":
    try:
        loop.create_task(task_schedule())
        loop.run_forever()
    except KeyboardInterrupt:
        print("EXIT😹😹😹😹😹")
    finally:
        loop.close()
