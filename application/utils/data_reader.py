import json
import csv

class DataReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r') as file:
            return list(csv.DictReader(file))
