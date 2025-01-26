import sys
input = sys.stdin.read().split('\n')
def display(grid:list[list[bool]]) -> None:
    for line in grid:
        toP = ''
        for pix in line:
            toP += '#' if pix else ' '
        print(toP)
disp = [[False] * 50 for _ in range(6)]
for action in input:
    splits = action.split()
    match splits[0]:
        case 'rect':
            x,y = list(map(int, splits[1].split('x')))
            for i in range(y):
                for j in range(x):
                    disp[i][j] = True
        case 'rotate':
            idx = int(splits[2].split('=')[1])
            inc = int(splits[-1])
            match splits[1]:
                case 'row':
                    rowCopy = disp[idx].copy()
                    for i in range(len(rowCopy)):
                        rowCopy[(i + inc) % len(rowCopy)] = disp[idx][i]
                    disp[idx] = rowCopy
                case 'column':
                    colCopy = [line[idx] for line in disp]
                    for i in range(len(colCopy)):
                        colCopy[(i + inc) % len(colCopy)] = disp[i][idx]
                    for i in range(len(colCopy)):
                        disp[i][idx] = colCopy[i]
                case _:
                    print('err')
        case _:
            print('err')

print(sum([sum([1 if px else 0 for px in line]) for line in disp]))