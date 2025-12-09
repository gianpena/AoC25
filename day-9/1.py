import sys

points = []

for line in sys.stdin:
    line = line.strip()
    line = list(map(int, line.split(',')))
    points.append(line)

for i in range(len(points)):
    k = points[i][0]
    points[i][0] = points[i][1]
    points[i][1] = k

max_area = -1

for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        dx = abs(points[i][0] - points[j][0]) + 1
        dy = abs(points[i][1] - points[j][1]) + 1
        max_area = max(max_area, dx * dy)

print(max_area)
