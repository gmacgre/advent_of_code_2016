import sys, re
from functools import reduce
input = sys.stdin.read().split('\n')
sectorIDs = 0
val = 'abcdefghijklmnopqrstuvwxyz'[::-1]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for code in input:
    room, checksum = re.split(r'\[|\]', code)[:2]
    holdName = room
    room = room.split('-')
    id = int(room.pop(len(room) - 1))
    room = reduce(lambda x,y : x + y, room)
    alpha = {}
    for char in room:
        if char not in alpha:
            alpha[char] = 0
        alpha[char] += 1
    checks = sorted(list(alpha.keys()), key=lambda x: alpha[x] + (val.index(x) / 100), reverse=True)
    if checksum == reduce(lambda x,y: x + y, checks[:5]):
        # Print the room's real name
        newName = ''
        for char in holdName:
            if char == '-':
                newName += ' '
                continue
            if char not in alphabet:
                break
            newName += alphabet[(alphabet.index(char) + id) % len(alphabet)]
        if 'pole' in newName:
            print(id)
            break