from cl_getter import get_clickers
from iter_cls import iter_cls

def prepare_status(res):
    if res.get("error"):
        return f"❌ Ошибка: {res['error']}"
    status = res["req"]["status"]
    if status == 502:
        return "🔄 Перезагрузить"
    elif status == 404:
        return "✅ Все с номером окей"
    return f"🤷‍♀️ С номером непонятки. Ответ от сервера{res["req"]}"

async def txt_analyze(DB_PATH):
    clickers = get_clickers(DB_PATH)
    data = await iter_cls(clickers)


    txt_data = ""

    for res in data:
        phone_str = f"Номер: {res["device"]["phone"]}, Порт: {res["device"]["port"]}, Сервер: {res["device"]["server"]}"
        txt_data+= f"{phone_str}\n"
        txt_data += prepare_status(res) + "\n\n"
    return txt_data

if __name__ == "__main__":
    from get_db_path import get_db_path
    import asyncio
    data = asyncio.run(txt_analyze(get_db_path()))

    with open("tech_analyse.txt", "w", encoding="utf-8") as f:
        f.write(data)
