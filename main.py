import pygame
import math
import random
from sys import exit
from player import Player
from ufo import Ufo
from utils import get_random_direction
from utils import rotate_x
from utils import rotate_y

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

class Asteroid:
    def __init__(self):
        self.pos = Vector2(0, 0)
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)
        self.finished = False

        if random.random() > 0.5:
            #start at the top
            self.start.x = random.randint(0, SCALE)
            self.start.y = -30
            self.end.x = random.randint(0, SCALE)
            self.end.y = SCALE + 30
            self.pos.x = self.start.x
            self.pos.y = self.start.y
        else:
            #start at the left and go right
            self.start.x = -30
            self.start.y = random.randint(0, SCALE)
            self.end.x = SCALE+30
            self.end.y = random.randint(0, SCALE)
            self.pos.x = self.start.x
            self.pos.y = self.start.y

        self.speed = random.randint(1, 4)
        self.asteroid = [Vector2(6, 3), Vector2(15, 5), Vector2(17, 0), Vector2(25, 4),
                         Vector2(26, 8), Vector2(25, 18), Vector2(28, 22), Vector2(17, 28), Vector2(6, 27), Vector2(0, 23), Vector2(2, 9)]

        for i in range(len(self.asteroid)):
            self.asteroid[i].x -= 14
            self.asteroid[i].y -= 14

        self.angle = random.randint(0, 270)

        rand = random.random()
        if rand < 0.25: self.scale = 0.25
        elif rand >= 0.25 and rand < 0.5: self.scale = 0.5
        elif rand >= 0.5 and rand < 0.75: self.scale = 0.75
        else: self.scale = 1

    def update(self):
        length = math.sqrt(pow(abs(self.end.x - self.pos.x), 2) + pow(abs(self.end.y - self.pos.y), 2))
        for i in range(self.speed):
            self.pos.x += (self.end.x-self.pos.x)/length
            self.pos.y += (self.end.y-self.pos.y)/length

            if(self.pos.x-2 < self.end.x and self.pos.x+2 > self.end.x and self.pos.y-2 < self.end.y and self.pos.y+2 > self.end.y):
                self.finished = True
                break

    def draw(self, surf):
        tmp_list = []
        for i in range(len(self.asteroid)):
            tmp_list.append(Vector2(rotate_x(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + self.pos.x, rotate_y(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + self.pos.y))

        pygame.draw.polygon(surf, 'white', tmp_list, 1)

class Asteroids:
    def __init__(self):
        self.list = []
        self.spawn_asteroid_in = random.randint(0, 200)
        self.spawn_cap = 10

    def update(self):
        if self.spawn_asteroid_in <= 0 and len(self.list) < self.spawn_cap:
            self.spawn_asteroid_in = random.randint(0, 200)
            self.list.append(Asteroid())
        else: self.spawn_asteroid_in -= 1

        for asteroid in self.list:
            asteroid.update()

        i = 0
        while i < len(self.list):
            if self.list[i].finished:
                self.list.pop(i)
                i = 0
            else: i += 1

    def draw(self, surf):
        for asteroid in self.list:
            asteroid.draw(surf)

asteroids = Asteroids()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    keys = pygame.key.get_pressed()

    asteroids.update()
    player.update(keys)

    #for ufo in ufos: ufo.update()

    # draw
    display.fill("black")

    asteroids.draw(display)
    player.draw(display)

    #for ufo in ufos: ufo.draw(display)

    screen.blit(pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGH)), (0, 0));
    pygame.display.update()
    clock.tick(60)
