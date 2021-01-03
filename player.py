from map import world_map, empty_map
from settings import *
import pygame
import random
from math import atan2, pi

SPAWN_POINT = random.choice(empty_map)


class Player:
    def __init__(self):
        self.x = SPAWN_POINT[0] + random.randint(5, 10)
        self.y = SPAWN_POINT[1] + random.randint(5, 10)
        self.angle = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        # Move player
        if keys[pygame.K_w]:
            if (self.x // TILE[0] * TILE[0], (self.y - SPEED - PLAYER_BOUNDER) // TILE[1] * TILE[1]) not in world_map:
                self.y -= SPEED
        if keys[pygame.K_s]:
            if (self.x // TILE[0] * TILE[0], (self.y + SPEED + PLAYER_BOUNDER) // TILE[1] * TILE[1]) not in world_map:
                self.y += SPEED
        if keys[pygame.K_a]:
            if ((self.x - SPEED - PLAYER_BOUNDER) // TILE[0] * TILE[0], self.y // TILE[1] * TILE[1]) not in world_map:
                self.x -= SPEED
        if keys[pygame.K_d]:
            if ((self.x + SPEED + PLAYER_BOUNDER) // TILE[0] * TILE[0], self.y // TILE[1] * TILE[1]) not in world_map:
                self.x += SPEED

    def rotate(self):
        cursor_position = pygame.mouse.get_pos()
        vec_x, vec_y = cursor_position[0] - self.x, cursor_position[1] - self.y
        self.angle = (180 / pi) - atan2(vec_x, vec_y)
