root_servers = {
    ("ws-" + ("0" if i < 10 else "") + str(i)): f"192.168.88.1"
    + ("0" if i < 10 else "")
    + str(i)
    for i in range(1, 11)
}
