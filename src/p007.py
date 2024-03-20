import json


def write_as_json(file_path, data):
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file)


def read_as_json(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)
