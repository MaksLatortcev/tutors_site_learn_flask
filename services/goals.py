import json


class Goals:
    """
    Класс, реализующий логику работы с данными о целях
    """
    # Пусть к файлу с данными
    path = None
    # Значки для целей
    emoji = {"travel": "⛱",
             "study": "🏫",
             "work": "🏢",
             "relocate": "🚜",
             "prog": "⌨"}

    def find_goals(self):
        """
        Функция, которая извлекает данные о всех целях
        :return: dict
        """
        with open(self.path, "r") as f:
            data = json.load(f)
            return data['goals']

    def names_goals(self):
        """
        Функция, которая извлекает русские названия целей и прикрепляет к них  значёк
        :return: dict
        """
        names = {}
        goals = self.find_goals()
        for key, val in goals.items():
            name = self.emoji[key] + " " + val
            temp_data = names.fromkeys([key], name)
            names.update(temp_data)

        return names
