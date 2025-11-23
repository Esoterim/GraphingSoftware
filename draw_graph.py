import pygame
from colors import Color

def draw_line(x1, y1, x2, y2, screen, color):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

def draw_grid(screen):
    draw_line(-400, 0, 400, 0, screen, Color.Black)

    draw_line(0, -400, 0, 400, screen, Color.Black)
    for i in range(-40, 40):
        j = i * 10
        draw_line(j, 5, j, -5, screen, Color.Black)
        draw_line(5, j, -5, j, screen, Color.Black)