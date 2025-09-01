import pygame
import math
from sys import exit
from player import Player

SCREEN_WIDTH = 1080
SCREEN_HEIGH = 1080
SCALE = 320

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
clock = pygame.time.Clock()

display = pygame.Surface((SCALE, SCALE))

player = Player(SCALE/2, SCALE/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # update
    keys = pygame.key.get_pressed()

    player.update(keys)

    # draw
    display.fill("black")

    player.draw(display)

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGH)), (0, 0));
    pygame.display.update()
    clock.tick(60)
