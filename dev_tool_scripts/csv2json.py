import csv
import json

def csv_to_json(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        return json.dumps([row for row in reader], indent=4)

csv_file = 'data.csv'
json_data = csv_to_json(csv_file)
print(json_data)
