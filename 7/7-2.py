import sys,re
input = sys.stdin.read().split('\n')

def getAba(line:str, found:set) -> bool:
    for i in range(len(line) - 2):
        if line[i] == line[i+2] and line[i+1] != line[i]:
            found.add(line[i:i+3])
    return found

def isValid(parts: list[str]) -> bool:
    abas = set()
    for i in range(1, len(parts), 2):
        getAba(parts[i], abas)
    for i in range(0, len(parts), 2):
        for found in list(getAba(parts[i], set())):
            conv = found[1] + found[0] + found[1]
            if conv in abas:
                return True
    return False

print(sum([1 if isValid(re.split(r'\]|\[', prospect)) else 0 for prospect in input]))
