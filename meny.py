from lagring import save_servers, export_csv
from kontroller import check_server, check_all_servers

VALID_ENVIRONMENT ["dev", "test", "prod"]

def find_server(servers, namn):
    """"Return the server with this namn, or None if it does not exist"""
    for server in servers:
        if server["namn"] == namn.lower():
            return server
        return None

def display_servers(servers, environment=None, search_text=None):
    filtered_servers = servers
    if environment:
        filtered_servers = [server for server in servers if server["miljo"] == environment]

    if search_text:
        search_text = search_text.lower()
        filtered_servers = [
            server for server in filtered_servers
            if search_text in server['namn'].lower()
            or search_text in server['address'].lower()
        ]

    if not filtered_servers:
        print("No servers found")
        return

    print(
        f"{'NAME':<15}{'ADDRESS':<15}{'ENVIRONMENT':<15}"
        f"{'ROLE':<15}{'STATUS':<15}LAST CHECKED"
    )
    print("_" * 100)
    for server in filtered_servers:
        print(
            f"{server['namn']:<15}{server['adress']:<15}{server['miljo']:<15}"
            f"{server['roll']:<15}{server['status']:<15}{server['senast_kontrollerad']}"
        )

def add_server(servers, data_file):
    name = input("Server name: ").strip()
    if not name:
        print("Server name cannot be empty")
        return
    if find_server(servers, name):
        print("A server with that name already exists")
        return

    address = input("Adress/API: ").strip()
    role = input('Role: ').strip()

    while True:
        environment = input("Environment (dev/test/prod): ").strip().lower()
        if environment  in VALID_ENVIRONMENTS:
            break
        print("Invalid environment. Enter dev, test, or prod.")

    servers.append({
        "namn": name,
        "adress": address,
        "miljo": environment,
        "roll": role,
        "status": "unknown",
        "senast_kontrollerad": ""
    })
    save_servers(servers, data_file)
    print(f"Server '{name}' has been added")

def remove_server(servers, data_file):
    name = input("Enter the Server name to remove: ").strip()
    server = find_server(servers, name)
    if server is None:
        print("Server not found")
        return
    if server["miljo"] == "prod":
        confirmation = input(
            f"WARNING: '{name}' is a production server. Type YES to remove it."
        ).strip()
        if confirmation != "YES":
            print("Removal cancelled.")
            return
    servers.remove(server)
    save_servers(servers, data_file)
    print(f"Server '{name}' has been removed")

def run_menu(servers, data_file):
    while True:
        print("\n=== SERVER INVENTORY TOOL ===")
        print("1. Display servers")
        print("2. Display servers in environment")
        print("3. Add server")
        print("4. Remove server")
        print("5. Check one server")
        print("6. Check all servers")
        print("7. Export CSV report")
        print("8. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_servers(servers)
        elif choice == "2":
            environment = input("Environment (dev/test/prod): ").strip().lower()
            if environment not in VALID_ENVIRONMENT:
                print("Invalid environment.")
            else:
                display_servers(servers, environment=environment)
        elif choice == "3":
            add_server(servers, data_file)
        elif choice == "4":
            remove_server(servers, data_file)
        elif choice == "5":
            name = input("Server name: ").strip()
            server = find_server(servers, name)
            if server is None:
                print("Server not found.")
            else:
                status = check_server(server)
                save_servers(servers, data_file)
                print(f"{name}: {status}")
        elif choice == "6":
            check_all_servers(servers)
            save_servers(servers, data_file)
        elif choice == "7":
            print(f"Report created: {export_csv(servers)}")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid menu option. choose a number between 1 and 8.")