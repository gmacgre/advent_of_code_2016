import sys, hashlib
id = sys.stdin.read()
password= ['X'] * 8
count = -1
while True:
    count += 1
    toHash = f'{id}{count}'
    output = hashlib.md5(toHash.encode()).hexdigest()
    if output.startswith('00000'):
        if not output[5].isdigit():
            continue
        loc = int(output[5])
        if loc > 7:
            continue
        if password[loc] != 'X':
            continue
        password[loc] = output[6]
        if 'X' not in password:
            break
    
print(''.join(password))