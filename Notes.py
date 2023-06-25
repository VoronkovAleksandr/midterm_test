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

    def delete_note(self, index_note) -> str:
        self.notes.remove(index_note)
        return 'Заметка удалена'

    def length(self):
        return len(self.notes)
