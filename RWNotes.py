
def write_notes(notes: list, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for note in notes:
            _string = '{0};{1};{2};{3}\n'.format(note.id, note.date_time, note.title, note.text)
            f.writelines(_string)

def read_notes(file_name: str):

    with open(file_name, 'r', encoding='utf-8') as f:
        list_notes = []
        data = f.read()
        data = data.split('\n')
        data.remove('')
        for _string in data:
            list_notes.append(_string.split(';'))
        return list_notes








