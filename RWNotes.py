from Notes import Notes


class RWNotes:
    _notes = list

    def write_notes(self, notes: Notes, file_name: str):
        with open(file_name, 'w', encoding='utf-8') as f:
            for note in notes:
                _string = '{0};{1};{2};{3}'.format(note.id, note.date_time, note.title, note.text)
                f.writelines(_string)

    def read_notes(self, notes: Notes, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.readline()
            data = list(map(lambda x: x.replase('\n', ''), data))





