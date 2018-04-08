# Game by Jacob Ditter and Emil Smith
# Menu Elements in part by Harrison@pythonprogramming.net
import pygame
import time
import random
 
pygame.init()
 
display_width = 800
display_height = 600
font = pygame.font.SysFont ("freesansbold.ttf", 72)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
yellow= (255, 255, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SlackMan')
clock = pygame.time.Clock()

first = pygame.image.load("media\FIRST.png")
koalafied = pygame.image.load("media\KOALAFIED.png")
redbacks = pygame.image.load("media\REDBACKS.png")
woodie = pygame.image.load("media\WOODIE_FLOWERS.png")
ditter = pygame.image.load('dotter.png')


def quitgame():
    pygame.quit()
    quit()


def smalltext(msg, x, y, w, h):
    smallText = pygame.font.Font("freesansbold.ttf", 32)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2), y + (h/2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()


def game_loop():
    intro = False
    gameDisplay.fill(yellow)
    smalltext("Welcome to SlackMan!", 150, 400, 200, 100)
    pygame.display.update()
    alive = True
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 32)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2), y + (h/2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('8bit.ttf',90)
        TextSurf, TextRect = text_objects("SlackMan", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start Game", 150, 400, 200, 100, green, bright_green, game_loop())
        button("Exit", 450, 400, 200, 100, red, bright_red, quitgame)

        pygame.display.update()

game_intro()
pygame.quit()
quit()
