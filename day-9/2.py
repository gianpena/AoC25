# This problem fucking sucks. Eric, you can do so much better than this, man (or whoever wrote this problem)


import sys
from shapely.geometry import Point, Polygon


points = []

for line in sys.stdin:
    line = line.strip()
    line = list(map(int, line.split(',')))
    # line[0],line[1] = line[1],line[0]
    points.append(line)

n = len(points)
poly = Polygon(points)

ans = -1
top = 248 # use this one to test against points above and to its left
bottom = 249 # use this one to test against points below and to its left
x_top, y_top = points[top]
x_bottom, y_bottom = points[bottom]
print(x_top, y_top)
print(x_bottom, y_bottom)

def valid(x1,y1,x2,y2):
    for y in range(min(y1,y2), max(y1,y2)+1):
        if not poly.covers(Point(x1,y)): return False
        if not poly.covers(Point(x2,y)): return False
    for x in range(min(x1,x2), max(x1,x2)+1):
        if not poly.covers(Point(x,y1)): return False
        if not poly.covers(Point(x,y2)): return False

    return True

for i in range(n):
    if i == top: continue

    x,y = points[i]
    if not (y >= y_top and x <= x_top):
        continue

    if not valid(x,y,x_top,y_top):
        continue

    l1 = abs(x-x_top) + 1
    l2 = abs(y-y_top) + 1
    ans = max(ans, l1 * l2)

for i in range(n):
    if i == bottom: continue

    x,y = points[i]
    if not (y <= y_bottom and x <= x_bottom):
        continue

    if not valid(x,y,x_bottom,y_bottom):
        continue

    l1 = abs(x-x_bottom) + 1
    l2 = abs(y-y_bottom) + 1
    ans = max(ans, l1 * l2)

print(ans)