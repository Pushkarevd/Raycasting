from settings import *
from map import world_map
from math import cos, sin
import pygame


def raycast(sc, x, y, angle):
    cur_angle = angle - FOV // 2
    for ray in range(NUMBERS_OF_RAYS):
        cos_x = cos(cur_angle)
        sin_y = sin(cur_angle)
        for depth in range(DEPTH_OF_VIEW):
            xo = x + depth * cos_x
            yo = y + depth * sin_y
            pygame.draw.line(sc, (0, 255, 0), (x, y), (xo, yo), 2)
            if (xo // TILE[0] * TILE[0], yo // TILE[1] * TILE[1]) in world_map:
                break
        cur_angle += FOV / NUMBERS_OF_RAYS
