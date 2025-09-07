import pygame
import math
from utils import Vector2
from utils import SCREEN_WIDTH
from utils import SCREEN_HEIGHT
from utils import SCALE
from utils import COLOR_ON

class Bullet:
    def __init__(self, x, y, dx, dy, who_fired):
        self.pos = Vector2(x, y)
        self.dir = Vector2(dx, dy)
        self.speed = 6
        self.who_fired = who_fired
        self.out_of_bounds = False
        self.remove_me = False

    def update(self):
        self.pos.x += self.dir.x * self.speed
        self.pos.y += self.dir.y * self.speed

        if self.pos.x < 0 or self.pos.x > SCALE or self.pos.y < 0 or self.pos.y > SCALE:
            self.out_of_bounds = True

    def draw(self, surf):
        pygame.draw.line(surf, COLOR_ON, self.pos, (self.pos.x + self.dir.x*2, self.pos.y + self.dir.y*2))

    def get_mask(self):
        tmp_surf = pygame.Surface((10, 10))
        pygame.draw.line(tmp_surf, 'white', (5, 5), (self.dir.x*2 + 5, self.dir.y*2 + 5))
        tmp_surf.set_colorkey('#000000')
        return pygame.mask.from_surface(tmp_surf)

class Bullets:
    def __init__(self):
        self.list = []

    def update(self):
        for bullet in self.list:
            bullet.update()

        i = 0
        while i < len(self.list):
            if self.list[i].out_of_bounds or self.list[i].remove_me:
                self.list.pop(i)
                i = 0
            else: i += 1

    def draw(self, surf):
        for bullet in self.list:
            bullet.draw(surf)
