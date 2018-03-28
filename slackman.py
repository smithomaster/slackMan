import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
finished = False
start = False
drawn = False

while not finished:
    if not drawn:
        pygame.draw.rect(screen, (0,128,255), pygame.Rect(200, 200, 400, 400))
        drawn = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
    pygame.display.flip()

pygame.quit()
