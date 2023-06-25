
class Command:
    description: str
    menu: object
    my_description = ''

    def __init__(self, menu):
        self.description = self.my_description
        self.menu = menu

    def get_description(self):
        return self.description


class AddNote(Command):
    my_description = 'Добвить заметку'

    def execute(self):
        # self.service.add_note()
        pass


class ReadNote(Command):
    my_description = 'Прочитать заметку'

    def execute(self):
        pass


class EditNote(Command):
    my_description = 'Редактировать заметку'

    def execute(self):
        pass


class DeleteNote(Command):
    my_description = 'Удалить заметку'

    def execute(self):
        pass


class ReadNotes(Command):
    my_description = 'Удалить заметку'

    def execute(self):
        pass


class SaveNotes(Command):
    my_description = 'Созранить заметки'

    def execute(self):
        pass


class LoadNotes(Command):
    my_description = 'Загрузить заметки'

    def execute(self):
        pass


class Finish(Command):
    my_description = 'Завершить работу'

    def execute(self):
        self.menu.finish()
