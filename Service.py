from Note import Note
from Notes import Notes
from datetime import datetime
from RWNotes import read_notes, write_notes

class Service:
    note: Note
    notes: Notes

    def __init__(self):
        self.notes = Notes()
        pass

    def add_note(self) -> None:
        title = input('Введите заголовок: ')
        text = input('Введите заметку: ')
        if self.notes.length() == 0:
            id_note = 1
        else:
            index_last_note = self.notes.length() - 1
            last_note = self.notes.get_note(index_last_note)
            id_last_note = last_note.get_id()
            id_note = id_last_note + 1
        date_time = str(datetime.now().strftime("%d-%m-%y %H:%M"))
        note = Note(id=id_note, date_time=date_time, title=title, text=text)
        self.notes.create_note(note)

    def edit_note(self):
        try:
            id_note = int(input('Введите номер заметки: '))
            index_note = self.get_index_note_by_id(id_note)
            if index_note == -1:
                print('Заметки с таким номером не существует')
            else:
                title = input('Введите новый заголовок: ')
                text = input('Введите новую заметку: ')
                date_time = str(datetime.now().strftime("%d-%m-%y %H:%M"))
                note = Note(id=id_note, date_time=date_time, title=title, text=text)
                self.notes.update_note(index_note, note)
        except:
            print('Вы ввели неверные данные')

    def read_note(self):
        try:
            id_note = int(input('Введите номер заметки: '))
            index_note = self.get_index_note_by_id(id_note)
            if index_note == -1:
                print('Заметки с таким номером не существует')
            else:
                return print(self.notes.get_note(index_note))
        except:
            print('Вы ввели неверные данные')

    def delete_note(self):
        try:
            id_note = int(input('Введите номер заметки: '))
            index_note = self.get_index_note_by_id(id_note)
            if index_note == -1:
                print('Заметки с таким номером не существует')
            else:
                print(index_note)
                self.notes.delete_note(index_note)
                print('Заметка № {0} удалена'.format(id_note))
        except:
            print('Вы ввели неверные данные')

    def read_notes(self):
        for note in self.notes.get_notes():
            print(note)

    def get_index_note_by_id(self, id_note) -> Note:
        return self.notes.get_index_note_by_id(id_note)

    def save_notes(self):
        file_name = 'notes.txt'
        write_notes(self.notes.get_notes_as_notes(), file_name)

    def load_notes(self):
        file_name = 'notes.txt'
        list_notes = read_notes(file_name)
        self.notes.clear_notes()
        for note in list_notes:
            note = Note(id=int(note[0]), date_time=note[1], title=note[2], text=note[3])
            self.notes.create_note(note)

