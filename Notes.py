from Note import Note


class Notes:
    notes: list[Note]

    def __init__(self):
        self.notes = []

    def create_note(self, note: Note) -> None:
        self.notes.append(note)

    def get_note(self, index_note: int) -> Note:
        return self.notes[index_note]

    def get_notes(self) -> list[str]:
        lst_notes = []
        if len(self.notes):
            for i in range(0, len(self.notes)):
                lst_notes.append(self.get_note(i).get_note())
        else:
            lst_notes = ['У Вас нет заметок']
        return lst_notes

    def update_note(self, index_note: int, new_note: Note) -> str:
        self.notes[index_note] = new_note
        return 'Заметка обновлена'

    def delete_note(self, index_note):
        self.notes.pop(index_note)
        return 'Заметка удалена'

    def length(self):
        return len(self.notes)

    def find_note_by_id(self, id_note: int) -> Note:
        for note in self.notes:
            if note.get_id() == id_note: return note

    def get_index_note_by_id(self, id_note):
        for i in range (0, len(self.notes)):
            if self.notes[i].get_id() == id_note: return i
        return -1
    def get_notes_as_notes(self):
        return self.notes

    def clear_notes(self):
        self.notes.clear()
