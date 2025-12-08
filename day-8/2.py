import sys

boxes = []
for line in sys.stdin:
    line = line.strip()
    line = map(int, line.split(','))
    boxes.append(list(line))

n = len(boxes)

def distance(x1,y1,z1, x2, y2, z2):
    return (x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2

parents = [i for i in range(n)]
size = [1] * n
all_pairs = []

for i in range(n-1):
    for j in range(i+1, n):
        all_pairs.append((i,j, distance(*boxes[i], *boxes[j])))

all_pairs.sort(key=lambda k: k[2])

def find(i):
    if parents[i] == i:
        return i

    parents[i] = find(parents[i])
    return parents[i]

def unite(i,j):
    i = find(i)
    j = find(j)
    if i == j:
        return False

    if size[i] > size[j]:
        parents[j] = i
        size[i] += size[j]
    else:
        parents[i] = j
        size[j] += size[i]

    return True


for i in range(len(all_pairs)):
    a,b = all_pairs[i][:2]
    unite(a,b)
    if max(size[find(a)], size[find(b)]) == len(boxes):
        print(boxes[a][0] * boxes[b][0])
        break
