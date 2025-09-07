import pygame
from utils import rotate_x
from utils import rotate_y
from utils import SCALE
from utils import SCREEN_WIDTH
from utils import SCREEN_HEIGHT
from utils import Vector2
from bullet import Bullet
from asteroid import Asteroid
from utils import COLOR_ON
from utils import COLOR_OFF

class Player:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.dir = Vector2(0, 0)
        self.angle = 0
        self.boost = 2
        self.velocity = 0
        self.velocity_decrease = 0.025
        self.rotation_sensitivity = 0.075
        self.ship = [Vector2(0, -7), Vector2(-5, 7),  Vector2(5, 7)]
        self.mask = self.get_mask()
        self.dead = False
        self.dead_pixels = []
        self.dead_pixels_dir = []
        self.dead_timer = 0
        self.fire_cooldown = 0
        self.fire_cooldown_time = 15

    def get_rotated_ship(self, pos: Vector2):
        vecs = []
        for vec in self.ship:
            vecs.append(Vector2(rotate_x(vec.x, vec.y, self.angle) + pos.x, rotate_y(vec.x, vec.y, self.angle) + pos.y))

        return vecs

    def get_mask(self):
        tmp_surf = pygame.Surface((30, 30))
        vecs = self.get_rotated_ship(Vector2(14, 14))
        pygame.draw.polygon(tmp_surf, 'white', vecs)
        tmp_surf.set_colorkey('#000000')
        return pygame.mask.from_surface(tmp_surf)

    def respawn(self):
        self.pos = Vector2(SCALE/2, SCALE/2)
        self.angle = 0
        self.dir = Vector2(0, 0)
        self.velocity = 0
        self.dead = False
        self.dead_timer = 0
        self.dead_pixels = []
        self.dead_pixels_dir = []
        self.fire_cooldown = 0

    def update(self, keys, asteroids, bullets):
        if self.dead:
            if self.dead_timer > 0:
                self.dead_timer -= 1
                for i in range(len(self.dead_pixels)):
                    self.dead_pixels[i].x += self.dead_pixels_dir[i].x * 2
                    self.dead_pixels[i].y += self.dead_pixels_dir[i].y * 2
            else:
                self.respawn()

            return

        self.dir.x = rotate_x(0, -1, self.angle)
        self.dir.y = rotate_y(0, -1, self.angle)
        if(keys[pygame.K_SPACE] and self.velocity <= 0):
            self.velocity = self.boost

        if(keys[pygame.K_a]): self.angle -= self.rotation_sensitivity
        elif(keys[pygame.K_d]): self.angle += self.rotation_sensitivity

        if(self.velocity > 0):
            self.pos.x += self.dir.x * self.velocity
            self.pos.y += self.dir.y * self.velocity
            self.velocity -= self.velocity_decrease

        self.mask = self.get_mask()

        #mouse_pos = pygame.mouse.get_pos()
        #self.pos.x = mouse_pos[0]/(SCREEN_WIDTH/SCALE)
        #self.pos.y = mouse_pos[1]/(SCREEN_HEIGHT/SCALE)

        if keys[pygame.K_w] and self.fire_cooldown <= 0:
            self.fire_cooldown = self.fire_cooldown_time
            bullets.list.append(Bullet(self.pos.x, self.pos.y, self.dir.x, self.dir.y, 'player'))
        elif self.fire_cooldown > 0: self.fire_cooldown -= 1

        # check collisions
        for ast in asteroids:
            if self.mask.overlap(ast.mask, (ast.pos.x - self.pos.x, ast.pos.y - self.pos.y)):
                self.dead = True
                self.dead_timer = 120
                tmp_surf = pygame.Surface((30, 30))
                vecs = self.get_rotated_ship(Vector2(14, 14))
                pygame.draw.polygon(tmp_surf, 'white', vecs, 1)
                dx, dy = ast.get_dir()
                for i in range(0, 30):
                    for j in range(0, 30):
                        if tmp_surf.get_at((j, i)) == pygame.Color(255, 255, 255):
                            if j < 15 and i < 15: self.dead_pixels_dir.append(Vector2(-1, -1))
                            elif j >= 15 and i < 15: self.dead_pixels_dir.append(Vector2(1, -1))
                            elif j >= 15 and i >= 15: self.dead_pixels_dir.append(Vector2(1, 1))
                            elif j < 15 and i >= 15: self.dead_pixels_dir.append(Vector2(-1, 1))
                            self.dead_pixels.append(Vector2(j-14, i-14))

        for i in range(len(bullets.list)):
            if self.mask.overlap(bullets.list[i].get_mask(), (bullets.list[i].pos.x+10 - self.pos.x, bullets.list[i].pos.y+10 - self.pos.y)) and not bullets.list[i].who_fired == 'player':
                self.dead = True
                bullets.list[i].remove_me = True

    def draw(self, surf: pygame.Surface):
        if self.dead:
            for vec in self.dead_pixels:
                pygame.draw.rect(surf, COLOR_ON, [vec.x + self.pos.x, vec.y + self.pos.y, 1, 1])
            return
        vecs = self.get_rotated_ship(self.pos)

        pygame.draw.polygon(surf, COLOR_ON, vecs, 1)
