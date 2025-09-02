import pygame

Vector2 = pygame.math.Vector2

class Ufo:
    def __init__(self, x, y, dx, dy):
        self.pos = pygame.Vector2(x, y)
        self.dir = pygame.Vector2(dx, dy)
        self.away = False
        self.speed = 2
        self.ufo = [Vector2(12, 0), Vector2(13, 0), Vector2(14, 0), Vector2(15, 0), Vector2(16, 0), Vector2(17, 0), Vector2(18, 0), Vector2(19, 0), Vector2(20, 0), Vector2(21, 0), Vector2(22, 0), Vector2(23, 0), Vector2(24, 0), Vector2(25, 0),
                    Vector2(11, 1), Vector2(26, 1),
                    Vector2(10, 2), Vector2(27, 2),
                    Vector2(9, 3), Vector2(28, 3),
                    Vector2(9, 4), Vector2(28, 4),
                    Vector2(7, 5), Vector2(8, 5), Vector2(9, 5), Vector2(10, 5), Vector2(11, 5), Vector2(12, 5), Vector2(13, 5), Vector2(14, 5), Vector2(15, 5), Vector2(16, 5), Vector2(17, 5), Vector2(18, 5), Vector2(19, 5), Vector2(20, 5), Vector2(21, 5), Vector2(22, 5), Vector2(23, 5), Vector2(24, 5), Vector2(25, 5), Vector2(26, 5), Vector2(27, 5), Vector2(28, 5), Vector2(29, 5), Vector2(30, 5),
                    Vector2(6, 6), Vector2(7, 6), Vector2(30, 6), Vector2(31, 6),
                    Vector2(5, 7), Vector2(6, 7), Vector2(31, 7), Vector2(32, 7),
                    Vector2(4, 8), Vector2(5, 8), Vector2(32, 8), Vector2(33, 8),
                    Vector2(3, 9), Vector2(4, 9), Vector2(33, 9), Vector2(34, 9),
                    Vector2(2, 10), Vector2(3, 10), Vector2(34, 10), Vector2(35, 10),
                    Vector2(1, 11), Vector2(2, 11), Vector2(35, 11), Vector2(36, 11),
                    Vector2(0, 12), Vector2(1, 12), Vector2(2, 12), Vector2(3, 12), Vector2(4, 12), Vector2(5, 12), Vector2(6, 12), Vector2(7, 12), Vector2(8, 12), Vector2(9, 12), Vector2(10, 12), Vector2(11, 12), Vector2(12, 12), Vector2(13, 12), Vector2(14, 12), Vector2(15, 12), Vector2(16, 12), Vector2(17, 12), Vector2(18, 12), Vector2(19, 12), Vector2(20, 12), Vector2(21, 12), Vector2(22, 12), Vector2(23, 12), Vector2(24, 12), Vector2(25, 12), Vector2(26, 12), Vector2(27, 12), Vector2(28, 12), Vector2(29, 12), Vector2(30, 12), Vector2(31, 12), Vector2(32, 12), Vector2(33, 12), Vector2(34, 12), Vector2(35, 12), Vector2(36, 12), Vector2(37, 12),
                    Vector2(7, 13), Vector2(31, 13),
                    Vector2(7, 14), Vector2(8, 14), Vector2(30, 14), Vector2(31, 14),
                    Vector2(8, 15), Vector2(9, 15), Vector2(29, 15), Vector2(30, 15),
                    Vector2(9, 16), Vector2(10, 16), Vector2(28, 16), Vector2(29, 16),
                    Vector2(10, 17), Vector2(11, 17), Vector2(12, 17), Vector2(26, 17), Vector2(27, 17), Vector2(28, 17),
                    Vector2(12, 18), Vector2(13, 18), Vector2(14, 18), Vector2(15, 18), Vector2(16, 18), Vector2(22, 18), Vector2(23, 18), Vector2(24, 18), Vector2(25, 18), Vector2(26, 18),
                    Vector2(17, 19), Vector2(18, 19), Vector2(19, 19), Vector2(20, 19), Vector2(21, 19)]

    def update(self):
        self.pos.x += self.dir.x * self.speed
        self.pos.y += self.dir.y * self.speed

    def draw(self, surf):
        for vec in self.ufo:
            pygame.draw.rect(surf, 'white', [vec.x + self.pos.x, vec.y + self.pos.y, 1, 1])


