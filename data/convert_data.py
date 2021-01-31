
'''
Скрипт для конвертирования мок-данных из data.py в data.json
'''

import json
from data import goals, teachers

path = "/home/maks/PycharmProjects/tutors_site_learn_flask/data/data.json"
contents = {"goals": goals, "teachers": teachers}


with open(path, "w") as f:
    data = json.dump(contents, f)



