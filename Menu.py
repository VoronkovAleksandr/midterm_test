from WorkMenu import WorkMenu

INPUT_ERROR = 'Вы ввели неверные данные'


def check_command(num_command: int, menu: WorkMenu):
    if menu.size() >= num_command > 0:
        return True
    else:
        print(INPUT_ERROR)


class Menu:
    start: bool
    menu: WorkMenu

    def __init__(self):
        self.start = True
        self.menu = WorkMenu(self)

    def start_me(self) -> None:
        while self.start:
            self.print_menu()
            self.execute()

    def print_menu(self):
        print(self.menu.print())

    def execute(self):
        try:
            num_command = int(input())
            if check_command(num_command, self.menu):
                self.menu.execute(num_command - 1)
        except:
            print(INPUT_ERROR)

    def finish(self):
        print('Пока!')
        self.start = False