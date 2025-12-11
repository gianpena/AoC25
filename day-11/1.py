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
def countPaths(node):
    if node == 'out':
        return 1

    ans = 0
    for neighbor in G[node]:
        ans += countPaths(neighbor)

    return ans

print(countPaths('you'))