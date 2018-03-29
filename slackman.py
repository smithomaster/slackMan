import pygame, sys
import pygameMenu
from pygameMenu.locals import *

window_width = 600
window_height = 600
font = "8bit"
title = "SlackMan"
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
menu = pygameMenu.Menu(screen, window_width=window_width, window_height=window_height, font=pygameMenu.fonts.FONT_NEVIS, title='Main Menu')
finished = False
start = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
    pygame.display.flip()

pygame.quit()
