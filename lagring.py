import csv
import json
import os
from datetime import datetime
from pathlib import Path


def get_data_file():
    """Read the data-file path from the environment, with a default."""
    return Path(os.getenv("INVENTORY_DATAFIL", "server.json.py"))

def load_servers(data_file):
    """Load servers from JSON. Return an empty list if the file is missing."""
    data_file = Path(data_file)
    if not data_file.exists():
        return []

    try:
        with data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            print("Warning: JSON data must be a list. Starting with an empty list.")
            return []
        return data
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not read data file : {error}")
        return []

def save_servers(servers, data_file):
    data_file = Path(data_file)
    data_file.parent.mkdir(parents=True, exist_ok=True)
    with data_file.open("w", encoding="utf-8") as file:
        json.dump(servers, file, indent=2, ensure_ascii=False)

def export_csv(servers):
    reports_directory = Path("reports")
    reports_directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports_path = reports_directory / f"inventory_{timestamp}.csv"

    fieldnames = [
        "namn", "adress", "miljo", "roll", "status", "senast_kontrollerad"
    ]
    with reports_path.open8("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(servers)

        return reports_path


