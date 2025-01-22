import sys, hashlib
id = sys.stdin.read()
password = ''
count = 0
while True:
    toHash = f'{id}{count}'
    output = hashlib.md5(toHash.encode()).hexdigest()
    if output.startswith('00000'):
        password += output[5]
        if len(password) == 8:
            break
    count += 1
print(password)