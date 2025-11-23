import pygame
import dots
from draw import *
import sys
import calculate
from colors import Color

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Graphing Software"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
pygame.display.set_icon(pygame.image.load('assets/icon.png'))


def update_screen():
    screen.fill(Color.White)
    pygame.display.flip()
    pygame.display.update()

def event_handler(event):
    if event.type == pygame.QUIT:
        try:
            pygame.quit()
            sys.exit()
        except:
            sys.exit()
        finally:
            return


def main():
    while True:
        for event in pygame.event.get():
            event_handler(event)
        update_screen()

if __name__ == '__main__':
    main()