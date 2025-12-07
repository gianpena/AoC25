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

dq = deque()
dq.append(start)
splits = 0
while dq:
    r,c = dq.popleft()
    r_,c_ = r+1, c
    if r_ >= len(grid): continue

    if grid[r_][c_] == '.':
        dq.append((r_,c_))
        continue

    if (r_,c_) in seen: continue

    seen.add((r_,c_))
    left_r,left_c = r+1,c-1
    right_r,right_c = r+1,c+1
    if 0 <= left_r < len(grid) and 0 <= left_c < len(grid[0]):
        dq.append((left_r, left_c))
    if 0 <= right_r < len(grid) and 0 <= right_c < len(grid[0]):
        dq.append((right_r, right_c))

    splits += 1

print(splits)