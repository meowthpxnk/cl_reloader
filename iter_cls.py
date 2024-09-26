from req import req
import asyncio
from bcolors import bcolors


async def iter_cls(phones):
    tasks = []

    # phones = [{"phone": "666", "port": "666", "server": "ws-01"}]

    for phone in phones:
        tasks.append(
            asyncio.ensure_future(
                req(phone["port"], phone["server"], phone["phone"])
            )
        )

    await asyncio.gather(*tasks, return_exceptions=True)

    res_data = []

    for idx, task in enumerate(tasks):
        phone = phones[idx]
        if task.exception():
            print(
                bcolors.WARNING + "WARN: " + bcolors.ENDC,
                f"Phone {phone['phone']}Exception ",
                task.exception(),
            )

            res_data.append(
                {"phone": phone["phone"], "error": f"{str(task.exception())}"}
            )

            continue

        data, status, text = task.result()

        res_data.append(
            {
                "device": phone,
                "req": {"status": status, "text": text, "data": data},
            }
        )

    return res_data
