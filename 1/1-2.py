import sys
input = sys.stdin.read().split(', ')
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
RIGHT_TURNS = [
    EAST,
    SOUTH,
    WEST,
    NORTH
]
LEFT_TURNS = [
    WEST,
    NORTH,
    EAST,
    SOUTH
]
mods = {
    NORTH: (-1,0),
    SOUTH: (1,0),
    EAST: (0,1),
    WEST: (0,-1),
}
hori, vert = [0,0]
dir = NORTH
visited = set()
runner = (0,0)
visited.add(runner)
location = None
for move in input:
    dist = int(move[1:])
    dir = LEFT_TURNS[dir] if move[0] == 'L' else RIGHT_TURNS[dir]
    mod = mods[dir]
    for _ in range(dist):
        runner = (runner[0] + mod[0], runner[1] + mod[1])
        if runner in visited:
            location = runner
            break
        visited.add(runner)
    if location != None:
        break
print(f'{abs(location[0]) + abs(location[1])}')