import sys
import pygame

from src.labyrinth import labyrinth

display_width = 1000
display_height = 1000
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
WHITE = (255, 255, 255)
DISPLAY.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = pygame.mouse.get_pos()
            if event.button == 1:
                lab = labyrinth(DISPLAY,50,50,20, pygame.display)
            if event.button == 3:
                pass
