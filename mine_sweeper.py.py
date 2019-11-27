import random

class MineSweeper():
    def __init__(self, rows=10, columns=10, mines=10):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.mines_list = []
        self.field = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.mask_field = [["#" for j in range(self.columns)] for i in range(self.rows)]


    def pr_field(self, array):
        string = "----"*self.columns
        print(string+string[0:5])
        for i in range(self.rows):
            print(string+string[0:5])
            print("|",*array[i],"|", sep = (" | "))
        print(string+string[0:5])


    def get_mined(self, a , b):
        self.mines_list = [(a,b)]
        while len(self.mines_list) != self.mines+1:
            x = random.randint(0,self.rows-1)
            y = random.randint(0,self.columns-1)
            tuple_coord = (x,y)
            if tuple_coord not in self.mines_list:
                self.mines_list.append(tuple_coord)
                self.field[tuple_coord[0]][tuple_coord[1]] = "*"
            else:
                continue

    def end_game(self, flag):
        if flag == False:
            for mine in self.mines_list[1:]:
                self.mask_field[mine[0]][mine[1]] = "*"
            self.pr_field(self.mask_field)
            print("Boom! Поражение!")
        else:
            for mine in self.mines_list[1:]:
                self.mask_field[mine[0]][mine[1]] = "!"
            self.pr_field(self.mask_field)
            print("Победа!")


    def set_number(self, x, y):
        counter = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i < 0 or j < 0 or j >= self.columns or i >= self.rows:
                    continue
                elif self.field[i][j] == "*":
                        counter+=1
        self.field[x][y] = counter
        return counter


    def count_mines(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if self.field[i][j] != "*":
                    self.set_number(i,j)


    def open_field(self, x, y):
        if x < 0 or y < 0 or y >= self.columns or x >= self.rows:
            return True

        elif self.field[x][y] == "*":
            flag = False
            self.end_game(flag)
            return False

        elif self.field[x][y] > 0:
            self.mask_field[x][y] = self.field[x][y]
            return True
        elif self.mask_field[x][y] != "#":
            return True
        elif self.field[x][y] == 0:
            self.mask_field[x][y] = self.field[x][y]

        self.open_field(x-1,y-1)
        self.open_field(x-1,y+1)
        self.open_field(x+1,y-1)
        self.open_field(x+1,y+1)
        self.open_field(x-1,y)
        self.open_field(x+1,y)
        self.open_field(x,y-1)
        self.open_field(x,y+1)
        return True

    def check_input(self):
        while True:
            try:
                a, b = (int(i) for i in input(
                "Через пробел ввести координаты Строки и Столбца (отсчет от нуля): "
                ).split())
                break
            except:
                print("Некорректный ввод!")
        return a, b

    def first_turn(self):
        a,b = self.check_input()
        self.get_mined(a, b)
        self.count_mines()
        self.open_field(a, b)
        self.pr_field(self.mask_field)


    def game(self):
        self.pr_field(self.mask_field)
        self.first_turn()
        if sum(1 for el in self.mask_field for i in el if i == "#") == self.mines:
            flag = True
            self.end_game(flag)
            return 0
        while True:
            a, b = self.check_input()
            result = new_field.open_field(a, b)
            if result == False:
                break
            self.pr_field(self.mask_field)
            if sum(1 for el in self.mask_field for i in el if i == "#") == self.mines:
                flag = True
                self.end_game(flag)
                break

if __name__ == "__main__":
    new_field = MineSweeper(10,10,15)
    new_field.game()


