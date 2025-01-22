import sys
input = sys.stdin.read().split('\n')
counters = []
for _ in range(len(input[0])):
    counters.append({})
for message in input:
    for i in range(len(message)):
        if message[i] not in counters[i]:
            counters[i][message[i]] = 0
        counters[i][message[i]] += 1

print(''.join(sorted(list(counter.keys()), key=lambda x : counter[x])[0] for counter in counters))