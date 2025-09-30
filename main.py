import pygame
import math
import random
from sys import exit
from player import Player
from ufo import Ufos
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

ufos = Ufos()
player = Player(SCALE/2, SCALE/2)
asteroids = Asteroids()
bullets = Bullets()

intro_screen = True

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
    if not intro_screen: ufos.update(bullets, score)

    # draw
    display.fill(COLOR_OFF)
    if intro_screen:
        title_font = pygame.font.Font('./megamax.ttf', 32)
        title_text = title_font.render('ASTEROIDS', False, COLOR_ON)
        display.blit(title_text, (SCALE/2 - title_text.get_width()/2, 40))

    asteroids.draw(display)
    player.draw(display)
    if not intro_screen: ufos.draw(display)
    bullets.draw(display)

    display.blit(font.render(str(score.get()), False, COLOR_ON), (5, 5))

    if player.moved: intro_screen = False

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0));
    pygame.display.update()
    clock.tick(60)
