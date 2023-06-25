from datetime import datetime


class Note:
    id: int
    date_time:  datetime
    title: str
    text: str

    def __init__(self, id: int, date_time: datetime, title: str, text: str):
        self.id = id
        self.date_time = date_time.strftime("%d-%m-%y %H:%M")
        self.title = title
        self.text = text

    def __str__(self):
        return 'Зметка №{0} \n' \
               'Дата создания: {1} \n' \
               'Заголовок: {2} \n' \
               'Содержание заметки: {3}\n' \
            .format(self.id, self.date_time, self.title, self.text)

    def get_id(self):
        return self.id

    def get_note(self):
        return [self.id, self.date_time, self.title, self.text]
