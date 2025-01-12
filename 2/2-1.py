import sys
def valid(loc, keypad):
    return loc[0] >= 0 and loc[0] < len(keypad[0]) and loc[1] >= 0 and loc[1] < len(keypad)

input = sys.stdin.read().split('\n')
code = ''
keypad = [
    [ '1', '2', '3' ],
    [ '4', '5', '6' ],
    [ '7', '8', '9' ],
]
mods = {
    'U':(-1, 0),
    'R':(0, 1),
    'D':(1, 0),
    'L':(0, -1),
}
loc = (1, 1) #Start at 5
for instr in input:
    for move in instr:
        m = mods[move]
        newLoc = (loc[0] + m[0], loc[1] + m[1])
        if valid(newLoc, keypad):
            loc = newLoc
    code += keypad[loc[0]][loc[1]]
print(code)