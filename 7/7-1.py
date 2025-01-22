import sys,re
input = sys.stdin.read().split('\n')

def hasAbba(line:str) -> bool:
    for i in range(len(line) - 3):
        substr = line[i:i+4]
        if  substr[0] == substr[-1] and \
            substr[1] == substr[-2] and \
            substr[0] != substr[1]:
            return True
    return False

def isValid(parts: list[str]) -> bool:
    for i in range(1, len(parts), 2):
        if hasAbba(parts[i]):
            return False
    for i in range(0, len(parts), 2):
        if hasAbba(parts[i]):
            return True
    return False

print(sum([1 if isValid(re.split(r'\]|\[', prospect)) else 0 for prospect in input]))
