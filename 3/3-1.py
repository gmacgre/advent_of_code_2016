import sys
input = sys.stdin.read().split('\n')
count = 0
for triangle in input:
    sides = sorted(list(map(int, triangle.split())))
    if sides[-1] < sides[0] + sides[1]:
        count += 1
print(count)
