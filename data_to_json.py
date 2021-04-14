import json

from data import goals, teachers


def data_to_json(data, file):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


data_to_json(goals, 'goals.json')
data_to_json(teachers, 'teachers.json')
