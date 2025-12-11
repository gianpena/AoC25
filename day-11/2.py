import sys
from functools import cache
from collections import defaultdict

G = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    line[0] = line[0][:-1]
    for node in line[1:]:
        G[line[0]].add(node)

@cache
def countPaths(node, visitedDAC, visitedFFT):
    if node == 'out':
        return int(visitedDAC and visitedFFT)

    ans = 0
    for neighbor in G[node]:
        ans += countPaths(neighbor, visitedDAC or node == 'dac', visitedFFT or node == 'fft')

    return ans

print(countPaths('svr', False, False))