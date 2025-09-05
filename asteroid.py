import pygame
import math
import random
from utils import rotate_x
from utils import rotate_y
from utils import SCALE
from utils import Vector2

class Asteroid:
    def __init__(self):
        self.pos = Vector2(0, 0)
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)
        self.finished = False

        rand = random.random()
        if rand < 0.25:
            #start at the top
            self.start.x = random.randint(0, SCALE)
            self.start.y = -30
            self.end.x = random.randint(0, SCALE)
            self.end.y = SCALE + 30
            self.pos.x = self.start.x
            self.pos.y = self.start.y
        elif rand >= 0.25 and rand < 0.5:
            #start at the left and go right
            self.start.x = -30
            self.start.y = random.randint(0, SCALE)
            self.end.x = SCALE+30
            self.end.y = random.randint(0, SCALE)
            self.pos.x = self.start.x
            self.pos.y = self.start.y
        elif rand >= 0.5 and rand < 0.75:
            #start at the bottom and go up
            self.start.x = random.randint(0, SCALE)
            self.start.y = SCALE+30
            self.end.x = random.randint(0, SCALE)
            self.end.y = -30
            self.pos.x = self.start.x
            self.pos.y = self.start.y
        elif rand >= 0.75:
            #start at the right and go left
            self.start.x = SCALE+30
            self.start.y = random.randint(0, SCALE)
            self.end.x = -30
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
        self.spawn_interval = 50
        self.spawn_asteroid_in = random.randint(0, self.spawn_interval)
        self.spawn_cap = 10

    def update(self):
        if self.spawn_asteroid_in <= 0 and len(self.list) < self.spawn_cap:
            self.spawn_asteroid_in = random.randint(0, self.spawn_interval)
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
