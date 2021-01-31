import os.path
import json
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, SelectField


class BookingForm(FlaskForm):
    """
    Класс, реализующий получение данных записи на урок к преподавателю
    """
    # Пусть к файлу с данными
    path = None
    # Параметры формы
    day = StringField()
    time = StringField()
    id_teacher = IntegerField()
    name = StringField('Вас зовут')
    phone = IntegerField('Ваш телефон')
    submit = SubmitField('Записаться на пробный урок')

    def save_booking_data(self):
        """
        Функция, которая сохранаяет данные о записи на урок в файл booking.json
        """
        client_name = self.name.data
        client_phone = self.phone.data
        client_day = self.day.data
        client_time = self.time.data
        id_teacher = self.id_teacher.data
        booking_data = [id_teacher,
                        client_day,
                        client_time,
                        client_name,
                        client_phone]

        if os.path.exists(f"{self.path}booking.json") is False:
            with open(f"{self.path}booking.json", "w", encoding='utf-8') as f:
                json.dump([booking_data], f)
        else:
            with open(f"{self.path}booking.json", "r", encoding='utf-8') as f:
                booking_data_story = json.load(f)

            booking_data_story.append(booking_data)

            with open(f"{self.path}booking.json", "w", encoding='utf-8') as f:
                json.dump(booking_data_story, f)

        return print('Сохранно в booking.json')


class RequestForm(FlaskForm):
    """
     Класс, реализующий получение данных заявок на подбор преподавателя.
    """
    # Пусть к файлу с данными
    path = None
    # параметры формы
    goal = RadioField('Какая цель занятий?',
                      choices=[('Для путешествий', 'Для путешествий'),
                               ('Для школы', 'Для школы'),
                               ('Для работы', 'Для работы'),
                               ('Для переезда', 'Для переезда')]
                      )
    time = RadioField('Сколько времени есть?',
                      choices=[('1-2 часа в неделю', '1-2 часа в неделю'),
                               ('3-5 часов в неделю', '3-5 часов в неделю'),
                               ('5-7 часов в неделю', '5-7 часов в неделю'),
                               ('7-10 часов внеделю', '7-10 часов внеделю')]
                      )
    name = StringField('Вас зовут')
    phone = IntegerField('Ваш телефон')
    submit = SubmitField('Найдите мне преподавателя')

    def save_request_data(self):
        """
        Функция, которая сохранаяет данные заявки на подбор преподавателя в файл request.json
        """
        client_name = self.name.data
        client_phone = self.phone.data
        client_goal = self.goal.data
        client_time = self.time.data
        request_data = [client_goal,
                        client_time,
                        client_name,
                        client_phone]

        if os.path.exists(f"{self.path}request.json") is False:
            with open(f"{self.path}request.json", "w", encoding='utf-8') as f:
                json.dump([request_data], f)
        else:
            with open(f"{self.path}request.json", "r", encoding='utf-8') as f:
                request_data_story = json.load(f)

            request_data_story.append(request_data)

            with open(f"{self.path}request.json", "w", encoding='utf-8') as f:
                json.dump(request_data_story, f)

        return print('Сохранно в request.json')


class SelectForm(FlaskForm):
    """
    Класс, реализующий фильтры для страницы со всеми преподавателями - /all/
    """
    filter = SelectField(choices=[('1', 'В случайном порядке'),
                                  ('2', 'Сначала лучшие по рейтингу'),
                                  ('3', 'Сначала дорогие'),
                                  ('4', 'Сначала недорогие')]
                         )
