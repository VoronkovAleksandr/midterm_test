
class Command:
    description: str
    my_description = ''

    def __init__(self, menu, service):
        self.description = self.my_description
        self.menu = menu
        self.service = service

    def get_description(self):
        return self.description


class AddNote(Command):
    my_description = 'Добавить заметку'

    def execute(self):
        print('Добавить заметку')
        self.service.add_note()


class ReadNote(Command):
    my_description = 'Прочитать заметку'

    def execute(self):
        print('Прочитать заметку')
        self.service.read_note()


class EditNote(Command):
    my_description = 'Редактировать заметку'

    def execute(self):
        print('Редактировать заметку')
        self.service.edit_note()


class DeleteNote(Command):
    my_description = 'Удалить заметку'

    def execute(self):
        print('Удалить заметку')
        self.service.delete_note()


class ReadNotes(Command):
    my_description = 'Прочитать все заметки'

    def execute(self):
        print('Прочитать все заметки')
        self.service.read_notes()


class SaveNotes(Command):
    my_description = 'Сохранить заметки'

    def execute(self):
        print('Сохранить заметки')
        self.service.save_notes()


class LoadNotes(Command):
    my_description = 'Загрузить заметки'

    def execute(self):
        print('Загрузить заметки')
        self.service.load_notes()


class Finish(Command):
    my_description = 'Завершить работу'

    def execute(self):
        self.menu.finish()
