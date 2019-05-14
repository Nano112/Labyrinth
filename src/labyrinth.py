from src.tile import tile
import random

class labyrinth:

    def __init__(self, display, largeur, hauteur, taille_case):
        self.grid = [[tile(display, x * taille_case, y * taille_case, taille_case) for x in range(0, largeur)] for y in
                     range(0, hauteur)]
        self.largeur = largeur
        self.hauteur = hauteur
        self.display = display

        self.movements = []
        self.x = 0
        self.y = 0
        self.solved = []
        self.create(0, 0)

    def create(self, start_x, start_y):
        x = start_x
        y = start_y
        movements = []
        self.grid[y][x].viewed = self.grid[y][x].viewed + 1
        while self.grid[start_y][start_x].viewed < 2:
            direction = self.get_free_direction(x, y)

            if direction is not None:

                self.grid[y][x].mur[direction] = False

                x, y = self.move(x, y, direction)
                self.grid[y][x].viewed = self.grid[y][x].viewed + 1
                self.grid[y][x].mur[(direction + 2) % 4] = False
                movements.append(direction)
            elif len(movements) != 0:
                mov = movements.pop()
                self.solved.append(mov)
                inv_dir = (mov + 2) % 4
                self.grid[y][x].viewed = self.grid[y][x].viewed + 1
                x, y = self.move(x, y, inv_dir)
                self.grid[y][x].viewed = self.grid[y][x].viewed + 1



    def create_one(self):
            direction = self.get_free_direction(self.x, self.y)
            if direction is not None:
                self.grid[self.y][self.x].mur[direction] = False
                self.x, self.y = self.move(self.x, self.y, direction)
                self.grid[self.y][self.x].viewed = self.grid[self.y][self.x].viewed + 1
                self.grid[self.y][self.x].mur[(direction + 2) % 4] = False
                self.movements.append(direction)
            elif len(self.movements) != 0:
                inv_dir = (self.movements.pop() + 2) % 4
                self.grid[self.y][self.x].viewed = self.grid[self.y][self.x].viewed + 1
                self.x, self.y = self.move(self.x, self.y, inv_dir)
                self.grid[self.y][self.x].viewed = self.grid[self.y][self.x].viewed + 1




    def move(self, x, y, d):
        if d == 0:
            return x - 1, y
        if d == 1:
            return x, y - 1
        if d == 2:
            return x + 1, y
        if d == 3:
            return x, y + 1

    # 0 = Gauche
    # 1 = Haut
    # 2 = Droite
    # 3 = Bas

    def get_free_direction(self, index_x, index_y):
        direction = self.random_directions()
        for i in range(0, 4):
            if self.direction_is_free(index_x, index_y, direction[i]):
                return direction[i]
        return None

    def direction_is_free(self, index_x, index_y, d):
        if d == 0 and index_x == 0:
            return False
        elif d == 2 and index_x == self.largeur-1:
            return False
        elif d == 1 and index_y == 0:
            return False
        elif d == 3 and index_y == self.largeur-1:
            return False
        if d == 0 and (self.grid[index_y][index_x - 1].viewed != 0):
            return False
        if d == 1 and (self.grid[index_y - 1][index_x].viewed != 0):
            return False
        if d == 2 and (self.grid[index_y][index_x + 1].viewed != 0):
            return False
        if d == 3 and (self.grid[index_y + 1][index_x].viewed != 0):
            return False
        return True

    def random_directions(self):
        direction = [0, 1, 2, 3]
        random.shuffle(direction)
        return direction


    def draw(self):
        for x in range(0, self.largeur):
            for y in range(0, self.hauteur):
                self.grid[y][x].draw()
