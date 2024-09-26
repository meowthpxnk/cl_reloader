import sqlite3
import json

from bcolors import bcolors
from root_servers import root_servers


from statuses import STATUS_ENUM


def db_get_data(db_path: str):
    request = "SELECT d.phone, d.server_id, d.port, d.clicker_status FROM devices as d WHERE d._is_active = TRUE AND d.state = 'ON'"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    request_result = list(cursor.execute(request))
    connection.close()
    return request_result


def get_clickers(db_path):
    final_data = []
    for clicker in db_get_data(db_path):
        server = (
            f"ws-{clicker[1] if clicker[1] > 9 else '0' + str(clicker[1])}"
        )

        if server not in root_servers:
            print(
                bcolors.WARNING
                + "WARN:"
                + bcolors.ENDC
                + f"server {server} is not supported"
            )
            continue

        final_data.append(
            {
                "phone": clicker[0],
                "server": server,
                "port": clicker[2],
                "status": STATUS_ENUM[clicker[3]],
            }
        )
    return final_data


if __name__ == "__main__":

    r = get_clickers("new_connector.db")
    print(json.dumps(r, indent=4))
