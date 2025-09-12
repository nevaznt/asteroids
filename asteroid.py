import pygame
import math
import random
from utils import rotate_x
from utils import rotate_y
from utils import SCALE
from utils import Vector2
from utils import COLOR_ON
from utils import COLOR_OFF

class Asteroid:
    def __init__(self):
        self.pos = Vector2(0, 0)
        self.start = Vector2(0, 0)
        self.end = Vector2(0, 0)
        self.finished = False
        self.break_me = False
        self.break_animation = 0
        self.break_animation_time = 300
        self.broken_pixels = []
        self.broken_pixels_dir = []
        self.broken_pixels_color = []

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

        self.speed = random.randint(0, 1) + random.random() + 0.1
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

        self.mask = self.create_mask()

    def create_mask(self):
        tmp_surf = pygame.Surface((30, 30))

        tmp_list = []
        for i in range(len(self.asteroid)):
            tmp_list.append(Vector2(rotate_x(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + 14, rotate_y(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + 14))
        pygame.draw.polygon(tmp_surf, 'white', tmp_list)
        tmp_surf.set_colorkey('#000000')

        return pygame.mask.from_surface(tmp_surf)

    def get_dir(self):
        length = math.sqrt(pow(abs(self.end.x - self.pos.x), 2) + pow(abs(self.end.y - self.pos.y), 2))
        return (self.end.x-self.pos.x)/length, (self.end.y-self.pos.y)/length

    def update(self, bullets):
        if self.break_me:
            if len(self.broken_pixels) == 0:
                self.break_animation = self.break_animation_time
                tmp_list = []
                tmp_surf = pygame.Surface((30, 30))
                for i in range(len(self.asteroid)):
                    tmp_list.append(Vector2(rotate_x(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + 14, rotate_y(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + 14))
                pygame.draw.polygon(tmp_surf, 'white', tmp_list, 1)
                tmp_circle = pygame.Surface((40, 40))
                pygame.draw.circle(tmp_circle, 'green', (20, 20), 20, 1)
                circle_point_list = []
                for i in range(40):
                    for j in range(40):
                        if tmp_circle.get_at((j, i)) == pygame.Color(0, 255, 0):
                            #tmp_circle.set_at((j, i), pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                            circle_point_list.append(Vector2(j, i))
                tmp_circle.set_colorkey('#000000')
                for i in range(0, 30):
                    for j in range(0, 30):
                        if tmp_surf.get_at((j, i)) == pygame.Color(255, 255, 255):
                            tmp_list = []
                            for v in range(len(circle_point_list)):
                                cir_x = circle_point_list[v].x+self.pos.x - 20
                                cir_y = circle_point_list[v].x+self.pos.y - 20
                                this_x = j + self.pos.x - 14
                                this_y = i + self.pos.y - 14
                                tmp_list.append(math.sqrt(abs(math.pow(cir_x-this_x, 2))+abs(math.pow(cir_y-this_y, 2))))
                            tmp_list_copy = tmp_list.copy()
                            tmp_list_copy.sort()
                            for v in range(len(tmp_list)):
                                if tmp_list_copy[0] == tmp_list[v] and circle_point_list[v].x != -999999 and tmp_list[v] != 0:
                                    self.broken_pixels_color.append(tmp_circle.get_at((int(circle_point_list[v].x), int(circle_point_list[v].y))))
                                    cir_x = circle_point_list[v].x+self.pos.x - 20
                                    cir_y = circle_point_list[v].x+self.pos.y - 20
                                    this_x = j + self.pos.x - 14
                                    this_y = i + self.pos.y - 14
                                    self.broken_pixels_dir.append(pygame.Vector3((cir_x-this_x)/tmp_list[v], (cir_y-this_y)/tmp_list[v], 2))
                                    circle_point_list[v].x = -999999
                                    self.broken_pixels.append(Vector2(j, i))
                                    break

            if self.break_animation > 0:
                self.break_animation -= 1
                for i in range(len(self.broken_pixels)):
                    self.broken_pixels[i].x += self.broken_pixels_dir[i].x * self.broken_pixels_dir[i].z
                    self.broken_pixels[i].y += self.broken_pixels_dir[i].y * self.broken_pixels_dir[i].z
            return

        dx, dy = self.get_dir()
        self.pos.x += dx * self.speed
        self.pos.y += dy * self.speed

        if(self.pos.x-2 < self.end.x and self.pos.x+2 > self.end.x and self.pos.y-2 < self.end.y and self.pos.y+2 > self.end.y):
            self.finished = True

        for i in range(len(bullets.list)):
            if self.mask.overlap(bullets.list[i].get_mask(), (bullets.list[i].pos.x+10 - self.pos.x, bullets.list[i].pos.y+10 - self.pos.y)):
                self.break_me = True
                bullets.list[i].remove_me = True

    def draw(self, surf):
        if self.break_me:
            for vec in self.broken_pixels:
                pygame.draw.rect(surf, 'white', [vec.x + self.pos.x - 14, vec.y + self.pos.y - 14, 1, 1])

            return

        tmp_list = []
        for i in range(len(self.asteroid)):
            tmp_list.append(Vector2(rotate_x(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + self.pos.x, rotate_y(self.asteroid[i].x, self.asteroid[i].y, self.angle)*self.scale + self.pos.y))

        pygame.draw.polygon(surf, COLOR_ON, tmp_list, 1)

class Asteroids:
    def __init__(self):
        self.list = []
        self.broken = []
        self.spawn_interval = 75
        self.spawn_asteroid_in = random.randint(0, self.spawn_interval)
        self.spawn_cap = 10

    def update(self, bullets):
        if self.spawn_asteroid_in <= 0 and len(self.list) < self.spawn_cap:
            self.spawn_asteroid_in = random.randint(0, self.spawn_interval)
            self.list.append(Asteroid())
        else: self.spawn_asteroid_in -= 1

        for asteroid in self.list:
            asteroid.update(bullets)

        for asteroid in self.broken:
            asteroid.update(bullets)

        for i in range(len(self.list)):
            if self.list[i].break_me:
                self.broken.append(self.list[i])

        i = 0
        while i < len(self.list):
            if self.list[i].finished or self.list[i].break_me:
                self.list.pop(i)
                i = 0
            else: i += 1

        i = 0
        while i < len(self.broken):
            if self.broken[i].break_animation == 0 and len(self.broken[i].broken_pixels) != 0:
                self.broken.pop(i)
                i = 0
            else: i += 1

    def draw(self, surf):
        for asteroid in self.list:
            asteroid.draw(surf)

        for asteroid in self.broken:
            asteroid.draw(surf)
