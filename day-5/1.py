import sys
intervals = []
addingToIntervals = True

def isFresh(id):
    fresh = False
    for a,b in intervals:
        fresh = fresh or a <= id <= b

    return int(fresh)

ans = 0
for line in sys.stdin:
    line = line.strip()
    if line == '':
        addingToIntervals = False
        continue

    if addingToIntervals:
        a,b = map(int, line.split('-'))
        intervals.append((a,b))
    else:
        ans += isFresh(int(line))

print(ans)