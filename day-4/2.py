import sys
grid = []
for line in sys.stdin:
    line = line.strip()
    grid.append([i for i in line])

def solve():
    d = [-1,0,1]
    n = len(grid)
    m = len(grid[0])
    locations = []
    for i in range(n):
        for j in range(m):

            if grid[i][j] != '@': continue
            adjacent = 0
            for dx in d:
                for dy in d:
                    if (dx,dy) == (0,0): continue
                    x,y = i+dx,j+dy
                    if not (0 <= x < n and 0 <= y < m): continue
                    adjacent += (grid[x][y] == '@')

            if adjacent < 4:
                locations.append((i,j))

    for x,y in locations:
        grid[x][y] = '.'

    return len(locations)

ans = 0
while (k := solve()) > 0:
    ans += k

print(ans)