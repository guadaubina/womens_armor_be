import json
import os

MOCK_ID_GET_ALL = 'get_ayuda'
MOCK_ID_POST = 'post_ayuda'


def read_mock_json(mock_file) -> str:
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json'))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json')

    with open(f"{path}\\{mock_file}.json", 'r') as file:
        return file.read()
