import sys
from collections import deque

grid = []
seen = set()
start = -1,-1
line_no = 0
for line in sys.stdin:
    line = line.strip()
    for i in range(len(line)):
        if line[i] == 'S':
            start = line_no, i
            break
    line_no += 1

    grid.append(line)

from functools import cache
@cache
def dp(r, c):
    if r == len(grid)-1: return 1

    r_,c_ = r+1, c
    if grid[r_][c_] == '.':
        return dp(r_,c_)

    return dp(r_, c_-1) + dp(r_, c_+1)

print(dp(*start))