import sys
input = sys.stdin.read().split(', ')
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
hori, vert = [0,0]
dir = NORTH
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
for move in input:
    dist = int(move[1:])
    dir = LEFT_TURNS[dir] if move[0] == 'L' else RIGHT_TURNS[dir]
    match dir:
        case 0:
            vert -= dist
        case 1:
            hori += dist
        case 2:
            vert += dist
        case 3:
            hori -= dist

print(f'{abs(hori) + abs(vert)}')