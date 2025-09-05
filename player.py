import pygame
from utils import rotate_x
from utils import rotate_y
from utils import Vector2

class Player:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.dir = Vector2(0, 0)
        self.angle = 0
        self.boost = 2
        self.velocity = 0
        self.velocity_decrease = 0.025
        self.movement_sensitivity = 0.05
        self.ship = [Vector2(0, -7), Vector2(-5, 7),  Vector2(5, 7)]

    def get_rotated_ship(self):
        vecs = []
        for vec in self.ship:
            vecs.append(Vector2(rotate_x(vec.x, vec.y, self.angle) + self.pos.x, rotate_y(vec.x, vec.y, self.angle) + self.pos.y))

        return vecs

    def update(self, keys):
        if(keys[pygame.K_SPACE] and self.velocity <= 0):
            self.dir.x = rotate_x(0, -1, self.angle)
            self.dir.y = rotate_y(0, -1, self.angle)
            self.velocity = self.boost

        if(keys[pygame.K_a]): self.angle -= self.movement_sensitivity
        elif(keys[pygame.K_d]): self.angle += self.movement_sensitivity

        if(self.velocity > 0):
            self.pos.x += self.dir.x * self.velocity
            self.pos.y += self.dir.y * self.velocity
            self.velocity -= self.velocity_decrease

    def draw(self, surf: pygame.Surface):
        vecs = self.get_rotated_ship()

        pygame.draw.polygon(surf, "white", vecs, 1)
