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
from utils import Score

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font('./megamax.ttf')

display = pygame.Surface((SCALE, SCALE))

score = Score()

#ufos = []
player = Player(SCALE/2, SCALE/2)
asteroids = Asteroids()
bullets = Bullets()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    keys = pygame.key.get_pressed()

    asteroids.update(bullets, score)
    player.update(keys, asteroids.list, bullets, score)
    bullets.update()

    #for ufo in ufos: ufo.update()

    # draw
    display.fill(COLOR_OFF)

    asteroids.draw(display)
    player.draw(display)
    bullets.draw(display)

    #for ufo in ufos: ufo.draw(display)

    display.blit(font.render(str(score.get()), False, COLOR_ON), (5, 5))

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0));
    pygame.display.update()
    clock.tick(60)
