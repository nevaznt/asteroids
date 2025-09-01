import pygame
from utils import rotate_x
from utils import rotate_y

Vector2 = pygame.math.Vector2

class Player:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.dir = Vector2(0, 0)
        self.angle = 0
        self.boost = 2
        self.velocity = 0
        self.velocity_decrease = 0.025
        self.movement_sensitivity = 0.05
        self.ship = [
                    Vector2(0, -7), Vector2(0, -6),
                    Vector2(-1, -5), Vector2(1, -5), Vector2(-1, -4), Vector2(1, -4),
                    Vector2(-2, -3), Vector2(2, -3), Vector2(-2, -2), Vector2(2, -2), Vector2(-2, -1), Vector2(2, -1),
                    Vector2(-3, 0), Vector2(3, 0), Vector2(-3, 1), Vector2(3, 1), Vector2(-3, 2), Vector2(3, 2),
                    Vector2(-4, 3), Vector2(4, 3), Vector2(-4, 4), Vector2(4, 4), Vector2(-4, 5), Vector2(4, 5),
                    Vector2(-5, 6), Vector2(5, 6),
                    Vector2(-5, 7), Vector2(-4, 7), Vector2(-3, 7), Vector2(-2, 7), Vector2(-1, 7), Vector2(0, 7),
                    Vector2(1, 7), Vector2(2, 7), Vector2(3, 7), Vector2(4, 7), Vector2(5, 7)]

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

        self.pos.x += self.dir.x * self.velocity
        self.pos.y += self.dir.y * self.velocity
        if(self.velocity > 0): self.velocity -= self.velocity_decrease

    def draw(self, surf: pygame.Surface):
        vecs = self.get_rotated_ship()

        pygame.draw.line(surf, "white", (vecs[0].x, vecs[0]. y), (vecs[26].x, vecs[26].y))
        pygame.draw.line(surf, "white", (vecs[26].x, vecs[26]. y), (vecs[36].x, vecs[36].y))
        pygame.draw.line(surf, "white", (vecs[36].x, vecs[36]. y), (vecs[0].x, vecs[0].y))
