import json
from random import choice


class Teachers:
    """
    Класс, реализующий логику работы с данными о преподавателях
    """
    # Пусть к файлу с данными
    path = None
    # Русские названия дней недели
    week = {'mon': 'Понедельник',
            'tue': 'Вторник',
            'wed': 'Среда',
            'thu': 'Четверг',
            'fri': 'Пятница',
            'sat': 'Суббота',
            'sun': 'Воскресенье'
            }

    def __init__(self, id):
        self.id = id

    def __find_teacher__(self):
        """
        Данная функция находит данные о преподавателе по id
        :return: dict
        """
        with open(self.path, "r") as f:
            data = json.load(f)

            for teacher in data['teachers']:
                if teacher['id'] == self.id:
                    return teacher

    def __find_goals__(self):
        """
        Данная функция находит данные о целях
        :return: dict
        """
        with open(self.path, "r") as f:
            data = json.load(f)
            return data['goals']

    def get_name(self):
        """
        Данная функция извлекает имя из словаря teacher
        :return: str
        """
        teacher = self.__find_teacher__()
        return teacher['name']

    def get_about(self):
        """
        Данная функция извлекает заметку преподавателя "о себе" из словаря teacher
        :return: str
        """
        teacher = self.__find_teacher__()
        return teacher['about']

    def get_rating(self):
        """
        Данная функция извлекает рэйтинг из словаря teacher
        :return: str
        """
        teacher = self.__find_teacher__()
        return teacher['rating']

    def get_picture(self):
        """
        Данная функция извлекает картинку-аватар из словаря teacher
        :return: str
        """
        teacher = self.__find_teacher__()
        return teacher['picture']

    def get_price(self):
        """
        Данная функция извлекает стоимость часа из словаря teacher
        :return: str
        """
        teacher = self.__find_teacher__()
        return teacher['price']

    def get_goals(self):
        """
        Данная функция извлекает цели из словаря teacher
        :return: list
        """
        teacher = self.__find_teacher__()
        goals = []
        for goal in teacher['goals']:
            goals.append(self.__find_goals__()[goal])
        return goals

    def get_free_time(self):
        """
        Данная функция извлекает свободные часы преподавателя из словаря teacher
        :return: dict
        """
        teacher = self.__find_teacher__()
        all_times = teacher['free']
        free_times = {}

        for i in all_times:
            times = []
            for key, val in all_times[i].items():
                if val is True:
                    times.append(key)

            temp_data = free_times.fromkeys([i], times)
            free_times.update(temp_data)

        return free_times


def __get_teachers__(teachers_id):
    """
    Данная функция подготавливает список преподавателей, убирая лишнии данные, для дальнейшего использования в функциях:
    get_goal_teachers и get_some_teachers.
    :param teachers_id: list идентификаторов преподавателей
    :return: list of dict
    """
    teachers = []
    for id in teachers_id:
        teacher = Teachers(id)
        teacher_name = teacher.get_name()
        teacher_about = teacher.get_about()
        teacher_rating = teacher.get_rating()
        teacher_picture = teacher.get_picture()
        teacher_price = teacher.get_price()

        teacher = {"name": teacher_name,
                   "about": teacher_about,
                   "rating": teacher_rating,
                   "picture": teacher_picture,
                   "price": teacher_price,
                   "id": id}

        teachers.append(teacher)

    return teachers


def get_goal_teachers(goal):
    """
    Данная функция извлекает из данных о преподавателях только тех, кто соответствует выбранной цели.
    :param goal: цель для занятия
    :return: list of dict
    """
    teachers_id = []
    with open(Teachers.path, "r") as f:
        data = json.load(f)
        for teacher in data['teachers']:
            if goal in teacher['goals']:
                teachers_id.append(teacher['id'])

    teachers = __get_teachers__(teachers_id)

    return teachers


def get_some_teachers(quantity=None):
    """
    Данная функция возвращает набор данные о некотором числе преподавателей,
    если число не указано, то данные всех преподавателей.
    Сортировка осуществляется случайным образом.
    :param quantity: количество преподавателей
    :return: list of dict
    """
    teachers_id = []
    with open(Teachers.path, "r") as f:
        data = json.load(f)
        for teacher in data['teachers']:
            teachers_id.append(teacher['id'])

    if quantity is not None:
        random_id = []
        for _ in range(quantity):
            choice_id = choice(teachers_id)
            random_id.append(choice_id)
            teachers_id.remove(choice_id)
        teachers = __get_teachers__(random_id)

    else:
        random_id = []
        for _ in range(len(teachers_id)):
            choice_id = choice(teachers_id)
            random_id.append(choice_id)
            teachers_id.remove(choice_id)
        teachers = __get_teachers__(random_id)

    return teachers
