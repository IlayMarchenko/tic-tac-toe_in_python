from colorama import Fore, init
from termcolor import colored


class Game:
    init()
    field_dict = {
        1: colored('1', 'green'),
        2: colored('2', 'green'),
        3: colored('3', 'green'),
        4: colored('4', 'green'),
        5: colored('5', 'green'),
        6: colored('6', 'green'),
        7: colored('7', 'green'),
        8: colored('8', 'green'),
        9: colored('9', 'green')
    }

    def print_field(self):
        print(f'\n {self.field_dict.get(1)} | {self.field_dict.get(2)} | {self.field_dict.get(3)} ')
        print(f'---+---+---')
        print(f' {self.field_dict.get(4)} | {self.field_dict.get(5)} | {self.field_dict.get(6)} ')
        print(f'---+---+---')
        print(f' {self.field_dict.get(7)} | {self.field_dict.get(8)} | {self.field_dict.get(9)} ')

    def x_turn(self):
        while True:
            try:
                x_turn = int(input('Select a cell on the field: '))
                if x_turn < 0 or x_turn > 9:
                    print('Sorry, but you can use only numbers from 0 to 9')
                elif self.field_dict[x_turn] == 'X' or self.field_dict[x_turn] == 'O':
                    print('Sorry, this cell is busy')
                else:
                    break
            except ValueError:
                print('Sorry, but you can use only numbers from 0 to 9')
        self.field_dict[x_turn] = colored('X', 'red')

    def o_turn(self):
        while True:
            try:
                o_turn = int(input('Select a cell on the field: '))
                if o_turn < 0 or o_turn > 9:
                    print('Sorry, but you can use only numbers from 0 to 9')
                elif self.field_dict[o_turn] == 'X' or self.field_dict[o_turn] == 'O':
                    print('Sorry, this cell is busy')
                else:
                    break
            except ValueError:
                print('Sorry, but you can use only numbers from 0 to 9')
        self.field_dict[o_turn] = colored('O', 'blue')

    def check_if_someone_win(self):
        i = 1
        for i in range(1, 10, 3):
            if self.field_dict[i] == self.field_dict[i+1] == self.field_dict[i+2]:
                self.print_field()
                print('game over')
                exit(0)
        i = 1
        for i in range(1, 4):
            if self.field_dict[i] == self.field_dict[i+3] == self.field_dict[i+6]:
                self.print_field()
                print('game over')
                exit(0)
        if self.field_dict[1] == self.field_dict[5] == self.field_dict[9]:
            self.print_field()
            print('game over')
            exit(0)
        if self.field_dict[3] == self.field_dict[5] == self.field_dict[7]:
            self.print_field()
            print('game over')
            exit(0)

    def check_if_draw(self):
        result = True
        for i in self.field_dict.values():
            if i != 'X' or i != 'O':
                result = False
        return result


if __name__ == '__main__':
    game = Game()
    counter = 0
    while True:
        game.print_field()
        if counter % 2 == 0:
            game.x_turn()
        else:
            game.o_turn()
        game.check_if_someone_win()
        if game.check_if_draw():
            print('Draw')
            exit(0)
        counter += 1


