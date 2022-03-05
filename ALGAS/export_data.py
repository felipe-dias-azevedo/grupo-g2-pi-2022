import csv
import json
from sqlite3 import Cursor

def export_to_csv(data: list):
    csv_file = open("data.csv", 'w')
    
    data_file = csv.writer(csv_file)
    
    data_file.writerows(data)
    
    csv_file.close()
    
def export_to_json(data: list):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)