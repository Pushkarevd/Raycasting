from settings import *

MAP = """#################
         #.........#.....#
         #..#####..#.....#
         #......##.#.....#
         #..#......#.....#
         #..#####.##.##.##
         #...............#
         #################"""

# world_map for walls and empty_map for SPAWN_POINT
world_map = []
empty_map = []
for i, row in enumerate(MAP.split()):
    for j, element in enumerate(row):
        if element == "#":
            world_map.append((j * TILE[0], i * TILE[1]))
        elif element == ".":
            empty_map.append((j * TILE[0], i * TILE[1]))