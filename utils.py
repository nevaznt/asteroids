import math
import random

def rotate_x(x, y, angle):
    return x*math.cos(angle)-y*math.sin(angle)

def rotate_y(x, y, angle):
    return x*math.sin(angle)+y*math.cos(angle)

def get_random_direction():
    return ((1-random.random())-0.5) * 2
