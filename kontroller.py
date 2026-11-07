import os
import subprocess
from datetime import datetime

def check_server(server):
    """Ping a server and uppdate its status and last-checked timestamp."""
    timeout = os.getenv("INVENTORY_PING_TIMEOUT", "3")

    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", timeout, server["address"]],
            capture_output=True,
            text=True,
            timeout=int(timeout) + 2,
            check=False,
        )
        server["status"] = "up" if result.returncode == 0 else "down"
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
        server["status"] = "down"

    server["last-checked"] = datetime.now(). strftime("%Y-%m-%d %H:%M:%S")
    return server["status"]

def check_all_servers(servers):
    if not servers:
        print("There are no servers to check.")
        return
    for server in servers:
        status = check_server(server)
        print(f"{server['namn']}: {status}")
