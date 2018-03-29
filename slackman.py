import pygame

window_width = 600
window_height = 600
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
finished = False
start = False
emil = 0

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        pygame.display.flip()

pygame.quit()
