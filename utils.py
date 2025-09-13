import math
import random
import pygame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1080
SCALE = 320
COLOR_ON = '#FFFFFF'
COLOR_OFF = '#000000'

class Score:
    def __init__(self):
        self.val = 0

    def add(self, num):
        self.val += num

    def reduce(self, percent):
        self.val = math.ceil(self.val*((100-percent)/100))

    def get(self):
        return int(self.val)

Vector2 = pygame.math.Vector2

def rotate_x(x, y, angle):
    return x*math.cos(angle)-y*math.sin(angle)

def rotate_y(x, y, angle):
    return x*math.sin(angle)+y*math.cos(angle)

def get_random_direction():
    return ((1-random.random())-0.5) * 2
