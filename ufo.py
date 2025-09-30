import pygame
import random
import math
from bullet import Bullet
from utils import Vector2
from utils import COLOR_ON
from utils import COLOR_OFF
from utils import SCALE

class Ufo:
    def __init__(self):
        self.pos = Vector2(0, 0)
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)

        self.set_start_end()

        self.broken_pixels = []
        self.broken_pixels_dir = []
        self.broken_timer = 0
        self.broken = False
        self.finished = False
        self.shoot_interval = 60
        self.shoot_in = self.shoot_interval
        self.speed = 1
        self.ufo = [( 8 ,  0 ), ( 9 ,  0 ), ( 10 ,  0 ), ( 11 ,  0 ), ( 7 ,  1 ), ( 12 ,  1 ), ( 6 ,  2 ), ( 13 ,  2 ), ( 6 ,  3 ),
                    ( 13 ,  3 ), ( 6 ,  4 ), ( 13 ,  4 ), ( 5 ,  5 ), ( 14 ,  5 ), ( 4 ,  6 ), ( 5 ,  6 ), ( 6 ,  6 ), ( 7 ,  6 ), ( 8 ,  6 ), ( 9 ,  6 ), ( 10 ,  6 ),
                    ( 11 ,  6 ), ( 12 ,  6 ), ( 13 ,  6 ), ( 14 ,  6 ), ( 15 ,  6 ), ( 3 ,  7 ), ( 16 ,  7 ), ( 1 ,  8 ), ( 2 ,  8 ), ( 17 ,  8 ), ( 18 ,  8 ),
                    ( 0 ,  9 ), ( 19 ,  9 ), ( 0 ,  10 ), ( 1 ,  10 ), ( 2 ,  10 ), ( 3 ,  10 ), ( 4 ,  10 ), ( 5 ,  10 ), ( 6 ,  10 ), ( 7 ,  10 ), ( 8 ,  10 ), ( 9 ,  10 ),
                    ( 10 ,  10 ), ( 11 ,  10 ), ( 12 ,  10 ), ( 13 ,  10 ), ( 14 ,  10 ), ( 15 ,  10 ), ( 16 ,  10 ), ( 17 ,  10 ), ( 18 ,  10 ), ( 19 ,  10 ), ( 0 ,  11 ),
                    ( 19 ,  11 ), ( 1 ,  12 ), ( 18 ,  12 ), ( 2 ,  13 ), ( 17 ,  13 ), ( 3 ,  14 ), ( 4 ,  14 ), ( 5 ,  14 ), ( 6 ,  14 ), ( 7 ,  14 ), ( 8 ,  14 ), ( 9 ,  14 ),
                    ( 10 ,  14 ), ( 11 ,  14 ), ( 12 ,  14 ), ( 13 ,  14 ), ( 14 ,  14 ), ( 15 ,  14 ), ( 16 ,  14 )]
        self.mask = self.create_mask()

    def create_mask(self):
        tmp_surf = pygame.Surface((30, 30))

        pygame.draw.polygon(tmp_surf, COLOR_ON, self.ufo)

        tmp_surf.set_colorkey('#000000')

        return pygame.mask.from_surface(tmp_surf)

    def set_start_end(self):
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

    def update(self, bullets, score):
        if self.broken:
            if len(self.broken_pixels) == 0:
                self.broken_timer = 120
                tmp_surf = pygame.Surface((30, 30))
                for vec in self.ufo:
                    pygame.draw.rect(tmp_surf, 'white', [vec[0], vec[1], 1, 1])
                for i in range(0, 30):
                    for j in range(0, 30):
                        if tmp_surf.get_at((j, i)) == pygame.Color(255, 255, 255):
                            if j < 10 and i < 7: self.broken_pixels_dir.append(Vector2(-1, -1))
                            elif j >= 10 and i < 7: self.broken_pixels_dir.append(Vector2(1, -1))
                            elif j >= 10 and i >= 7: self.broken_pixels_dir.append(Vector2(1, 1))
                            elif j < 10 and i >= 7: self.broken_pixels_dir.append(Vector2(-1, 1))
                            self.broken_pixels.append(Vector2(j, i))

            if self.broken_timer > 0:
                self.broken_timer -= 1
                for i in range(len(self.broken_pixels)):
                    self.broken_pixels[i].x += self.broken_pixels_dir[i].x * 2
                    self.broken_pixels[i].y += self.broken_pixels_dir[i].y * 2
            else:
                self.finished = True

            return

        length = math.sqrt(math.pow(self.end.x - self.pos.x, 2) + math.pow(self.end.y - self.pos.y, 2))
        self.pos.x += ((self.end.x - self.pos.x) / length) * self.speed
        self.pos.y += ((self.end.y - self.pos.y) / length) * self.speed

        if(self.pos.x-2 < self.end.x and self.pos.x+2 > self.end.x and self.pos.y-2 < self.end.y and self.pos.y+2 > self.end.y):
            self.set_start_end()

        if self.shoot_in <= 0:
            bullets.list.append(Bullet(self.pos.x+10, self.pos.y+7, 1, 1, 'ufo'))
            bullets.list.append(Bullet(self.pos.x+10, self.pos.y+7, -1, -1, 'ufo'))
            bullets.list.append(Bullet(self.pos.x+10, self.pos.y+7, 1, -1, 'ufo'))
            bullets.list.append(Bullet(self.pos.x+10, self.pos.y+7, -1, 1, 'ufo'))
            self.shoot_in = self.shoot_interval
        elif self.shoot_in > 0:
            self.shoot_in -= 1

        for i in range(len(bullets.list)):
            if self.mask.overlap(bullets.list[i].get_mask(), (bullets.list[i].pos.x+10 - self.pos.x-15, bullets.list[i].pos.y+10 - self.pos.y-20)) and bullets.list[i].who_fired != 'ufo':
                if bullets.list[i].who_fired == 'player': score.add(100)
                self.broken = True
                bullets.list[i].remove_me = True

    def draw(self, surf):
        if self.broken:
            for vec in self.broken_pixels:
                pygame.draw.rect(surf, COLOR_ON, [vec.x + self.pos.x, vec.y + self.pos.y, 1, 1])
            return

        for vec in self.ufo:
            pygame.draw.rect(surf, COLOR_ON, [vec[0] + self.pos.x, vec[1] + self.pos.y, 1, 1])

class Ufos:
    def __init__(self):
        self.list = []
        self.broken = []
        self.spawn_interval = 2000
        self.spawn_in = random.randint(math.floor(self.spawn_interval*0.25), self.spawn_interval)
        self.spawn_cap = 1

    def update(self, bullets, score):
        if self.spawn_in <= 0 and len(self.list) < self.spawn_cap:
            self.list.append(Ufo())
            self.spawn_in = random.randint(math.floor(self.spawn_interval*0.25), self.spawn_interval)
        elif self.spawn_in > 0 and len(self.list) < self.spawn_cap: self.spawn_in -= 1

        for ufo in self.list:
            ufo.update(bullets, score)

        i = 0
        while i < len(self.list):
            if self.list[i].broken:
                self.broken.append(self.list[i])
                self.list.pop(i)
                i = 0
            else: i += 1

        for ufo in self.broken:
            ufo.update(bullets, score)

        i = 0
        while i < len(self.broken):
            if self.broken[i].finished:
                self.broken.pop(i)
                i = 0
            else: i += 1

    def draw(self, surf):
        for ufo in self.list:
            ufo.draw(surf)

        for ufo in self.broken:
            ufo.draw(surf)
