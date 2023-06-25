from Note import Note
from Notes import Notes
from Menu import Menu
from datetime import datetime

class Service:
    note: Note
    notes: Notes
    menu: Menu

    def __init__(self):
        self.notes = Notes()
        pass

    def add_note(self, title: str, text: str) -> None:
        if self.notes.length() == 0:
            id_note = 1
        else:
            index_last_note = self.notes.length() - 1
            last_note = self.notes.get_note(index_last_note)
            id_last_note = last_note.get_id()
            id_note = id_last_note + 1
        note = Note(id=id_note, date_time=datetime.now(), title=title,  text=text)
        self.notes.create_note(note)

    def edit_note(self):
        pass

    def read_note(self, index_note: int):
        return self.notes.get_note(index_note)
        pass

    def delete_note(self):
        pass

    def read_notes(self):
        return self.notes.get_notes()

    def find_notes(self):
        pass

    def save_notes(self):
        pass

    def load_notes(self):
        pass
