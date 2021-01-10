import pygame


class tile:


    def __init__(self, display, position_x, position_y, size, viewed=0, mur=None, color=None):
        if mur is None:
            mur = [True, True, True, True]
        if color is None:
            color = 0, 0, 0
        self.display = display
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        # mur[0] = Gauche
        # mur[1] = Haut
        # mur[2] = Droite
        # mur[3] = Bas
        self.mur = mur
        self.color = color
        self.viewed = viewed
        self.colors = [
            [0, 0, 255],
            [255, 0, 0],
            [0, 255, 0],
            [0, 255, 0],
            [0, 255, 0],
        ]

    def draw(self):
        c0 = self.position_x, self.position_y
        c1 = self.position_x + self.size, self.position_y
        c2 = self.position_x + self.size, self.position_y + self.size
        c3 = self.position_x, self.position_y + self.size
        pygame.draw.rect(self.display, self.colors[self.viewed], (self.position_x , self.position_y, self.size, self.size))
        if self.mur[0]:
            pygame.draw.line(self.display, self.color, c3, c0)
        if self.mur[1]:
            pygame.draw.line(self.display, self.color, c0, c1)
        if self.mur[2]:
            pygame.draw.line(self.display, self.color, c1, c2)
        if self.mur[3]:
            pygame.draw.line(self.display, self.color, c2, c3)

