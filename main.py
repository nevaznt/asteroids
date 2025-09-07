import pygame
import math
import random
from sys import exit
from player import Player
from ufo import Ufo
from utils import get_random_direction
from utils import rotate_x
from utils import rotate_y
from asteroid import Asteroids
from bullet import Bullets
from bullet import Bullet
from utils import SCREEN_WIDTH
from utils import SCREEN_HEIGHT
from utils import SCALE
from utils import COLOR_ON
from utils import COLOR_OFF
from utils import Vector2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

display = pygame.Surface((SCALE, SCALE))

player = Player(SCALE/2, SCALE/2)

#ufos = []

asteroids = Asteroids()
bullets = Bullets()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    keys = pygame.key.get_pressed()

    asteroids.update(bullets)
    player.update(keys, asteroids.list, bullets)
    bullets.update()

    #for ufo in ufos: ufo.update()

    # draw
    display.fill(COLOR_OFF)

    asteroids.draw(display)
    player.draw(display)
    bullets.draw(display)

    #for ufo in ufos: ufo.draw(display)

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0));
    pygame.display.update()
    clock.tick(60)
