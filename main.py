import argparse
import sys

from lagring import get_data_file, load_servers, save_servers, export_csv
from kontroller import check_server, check_all_servers
from meny import run_menu, display_servers, find_server


def create_parser():
    parser = argparse.ArgumentParser(description='Server Inventory Tool - manage and monitor servers.')
    parser.add_argument("--list", action="store_true", help="Display all servers.")
    parser.add_argument("--environment", choices=["dev", "test", "prod"],
                        help="Filter servers by environment.")
    parser.add_argument("--check", metavar="NAME", help="Ping one server by name.")
    parser.add_argument("--check-all", action="store_true",
                        help="Ping all registered servers.")
    parser.add_argument("--export", action="store_true",
                        help="Export all servers to csv report.")
    parser.add_argument("--search", metavar="TEXT",
                        help="Search server names or IP address.")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    data_file = get_data_file()
    servers = load_servers(data_file)

    if not any(vars(args).values()):
        run_menu(servers, data_file)
        return 0

    if args.list or args.environment or args.search:
        display_servers(servers, environment=args.environment, search_text=args.search)
        return 0

    if args.check:
        server = find_server(servers, args.check)
        if server is None:
            print(f"Error: server '{args.check}' was not found.")
            return 1
        status = check_server(server)
        save_servers(servers, data_file)
        print(f"{server['namn']}: {status}")
        return 0 if status == "up" else 1

    if args.check_all:
        check_all_servers(servers)
        save_servers(servers, data_file)
        return 0 if all (s["status"] == "up" for s in servers) else 1

    if args.export:
        report_path = export_csv(servers)
        print(f"CSV report created: {report_path}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
