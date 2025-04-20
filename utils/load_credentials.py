import os
import csv

def load_credentials_from_csv(filename="credentials.csv"):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", filename)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row["username"], row["password"]) for row in reader]