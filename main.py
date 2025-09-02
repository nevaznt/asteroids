import pygame
import math
import random
from sys import exit
from player import Player
from ufo import Ufo
from utils import get_random_direction

SCREEN_WIDTH = 1080
SCREEN_HEIGH = 1080
SCALE = 320

Vector2 = pygame.math.Vector2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
clock = pygame.time.Clock()

display = pygame.Surface((SCALE, SCALE))

player = Player(SCALE/2, SCALE/2)

#ufos = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    keys = pygame.key.get_pressed()

    player.update(keys)

    #if random.randint(0, 100) == 10:
    #    ufos.append(Ufo(random.randint(0, SCALE), -10, get_random_direction(), 1))

    #for ufo in ufos: ufo.update()

    # draw
    display.fill("black")

    player.draw(display)

    #for ufo in ufos: ufo.draw(display)

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGH)), (0, 0));
    pygame.display.update()
    clock.tick(60)
