# Game by Jacob Ditter and Emil Smith
# Menu Elements in part by Harrison@pythonprogramming.net
# Wall collision code http://blog.cravenfamily.com/2009/03/running-into-walls-with-python-and.html, Prof. Craven

import pygame
from pygame.locals import *
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
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SlackMan')
clock = pygame.time.Clock()

first = pygame.image.load("media\FIRST.png")
koalafied = pygame.image.load("media\KOALAFIED.png")
redbacks = pygame.image.load("media\REDBACKS.png")
woodie = pygame.image.load("media\WOODIE_FLOWERS.png")
ditter = pygame.image.load('dotter.png')
 # This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,height,width,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((blue))
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Woodie(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Set speed vector
        self.change_x=400
        self.change_y=300

        # Set height, width
        self.image = pygame.image.load("media/WOODIE.png")
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
            # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
    # Find a new position for the player
    def is_collided_with(self, player):
        if self.rect.colliderect(player.rect):
            pygame.quit()
# This class represents the bar at the bottom that the player controls


class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Set speed vector
        self.change_x=0
        self.change_y=0

        # Set height, width
        self.image = pygame.image.load("media/KOALAFIED.png")
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
    # Find a new position for the player
    def update(self,walls):
        # Get the old position, in case we need to go back to it
        old_x=self.rect.topleft[0]
        old_y=self.rect.topleft[1]

        # Update position according to our speed (vector)
        new_x=old_x+self.change_x
        new_y=old_y+self.change_y

        # Put the player in the new spot
        self.rect.topleft = (new_x,new_y)

        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.topleft=(old_x,old_y)

 # This is the main function where our program begins
def main():
    score = 0
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
    # Set the title of the window
    pygame.display.set_caption('SlackMan the Great one to find Woodie Flowers')
    # Enable this to make the mouse dissappear when over our window
    #pygame.mouse.set_visible(0)
    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Create a surface we can draw on
    background = pygame.Surface(screen.get_size())
    # Used for converting color maps and such
    background = background.convert()
    # Fill the screen with a black background
    background.fill(black)

    # Create the player paddle object
    player = Player(10,10)
    movingsprites = pygame.sprite.RenderPlain((player))
    woodie = Woodie(360,250)
    woodies = pygame.sprite.RenderPlain((woodie))

    # Make the walls. (height, width, x_pos, y_pos)
    wall_list=[]
    wall_list.append(Wall(600,10,0,0)) # right end
    wall_list.append(Wall(10,790,10,0)) # top end
    wall_list.append(Wall(600,10,790,0)) # right end
    wall_list.append(Wall(10,790,10,590)) # bottom end
    wall_list.append(Wall(10, 80, 10, 50))
    wall_list.append(Wall(100, 10, 80, 60))

    walls=pygame.sprite.RenderPlain(wall_list)

    clock = pygame.time.Clock()

    while 1:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.changespeed(-3,0)
                if event.key == K_RIGHT:
                    player.changespeed(3,0)
                if event.key == K_UP:
                    player.changespeed(0,-3)
                if event.key == K_DOWN:
                    player.changespeed(0,3)

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    player.changespeed(3,0)
                if event.key == K_RIGHT:
                    player.changespeed(-3,0)
                if event.key == K_UP:
                    player.changespeed(0,3)
                if event.key == K_DOWN:
                    player.changespeed(0,-3)

        player.update(walls)
        woodie.is_collided_with(player)
        pygame.draw.rect(screen,black,(0,0,800,600))
        movingsprites.draw(screen)
        woodies.draw(screen)
        walls.draw(screen)
        pygame.display.flip()

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


# def game_loop():
#     intro = False
#     gameDisplay.fill(yellow)
#     smalltext("Welcome to SlackMan!", 150, 400, 200, 100)
#     pygame.display.update()
#     alive = True
#     while alive:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()


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

        button("Start Game", 150, 400, 200, 100, green, bright_green, main)
        button("Exit", 450, 400, 200, 100, red, bright_red, quitgame)

        pygame.display.update()

game_intro()
pygame.quit()
quit()
