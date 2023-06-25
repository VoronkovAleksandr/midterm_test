from Commands import *

class WorkMenu:
    command_list: list

    def __init__(self, menu, service):
        self.command_list = []
        self.command_list.append(AddNote(menu, service))
        self.command_list.append(ReadNote(menu, service))
        self.command_list.append(EditNote(menu, service))
        self.command_list.append(DeleteNote(menu, service))
        self.command_list.append(ReadNotes(menu, service))
        self.command_list.append(SaveNotes(menu, service))
        self.command_list.append(LoadNotes(menu, service))
        self.command_list.append(Finish(menu, service))

    def print(self) -> str:
        menu = ''
        for i in range(0, len(self.command_list)):
            menu += '{0}. {1} \n'.format(i + 1,  self.command_list[i].get_description())
        return menu

    def size(self) -> int:
        return len(self.command_list)

    def execute(self, num_command):
        self.command_list[num_command].execute()
