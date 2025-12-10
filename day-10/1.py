import sys

indicators = []
buttons = []
joltage = []

for line in sys.stdin:
    line = line.strip()
    line = line.split()

    bits = line[0][1:-1].replace('.', '0').replace('#', '1')
    bits = int(bits, 2)
    indicators.append((bits, len(line[0])-2))

    buttons.append([])

    for i in range(1, len(line)-1):
        mask = 0
        for j in line[i][1:-1].split(','):
            mask |= 1 << (indicators[-1][1] - int(j) - 1)
        buttons[-1].append(mask)
    joltage.append(line[-1][1:-1].split(','))

from collections import deque

def shortest(i):

    visited = set()
    q = deque()
    q.append((0, 0))
    visited.add(0)

    while q:
        cost,mask = q.popleft()
        if mask == indicators[i][0]: return cost
        for button in buttons[i]:
            if (mask ^ button) in visited: continue
            visited.add(mask ^ button)
            q.append((cost+1, mask^button))

    return -1

ans = 0
for i in range(len(indicators)):
    ans += shortest(i)

print(ans)