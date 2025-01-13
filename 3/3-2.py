import sys
input = sys.stdin.read().split('\n')
count = 0
for i in range(0, len(input), 3):
    fRow = list(map(int, input[i].split()))
    sRow = list(map(int, input[i+1].split()))
    tRow = list(map(int, input[i+2].split()))
    first = sorted([fRow[0], sRow[0], tRow[0]])
    second = sorted([fRow[1], sRow[1], tRow[1]])
    third = sorted([fRow[2], sRow[2], tRow[2]])
    for sides in [first, second, third]:
        if sides[-1] < sides[0] + sides[1]:
            count += 1
print(count)
