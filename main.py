import pygame

from player import Player
from raycasting import raycast
from settings import *
from map import world_map
from multiprocessing import Process

running = True

pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sc.fill((0, 0, 0))

    # Player functions
    player.movement()
    player.rotate()
    pygame.draw.circle(sc, (255, 0, 0), (player.x, player.y), PLAYER_BOUNDER)
    raycast(sc, player.x, player.y, player.angle)

    # Draw walls
    for block in world_map:
        pygame.draw.rect(sc, (255, 255, 255), (block[0], block[1], TILE[0], TILE[1]), 2)

    pygame.display.flip()
    clock.tick(FPS)
