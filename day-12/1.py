import sys

ans = 0
for line in sys.stdin:
    line = line.strip()
    line = line.split()

    dimensions = line[0][:-1].split('x')
    l,r = map(int,dimensions)

    pieces = sum(map(int, line[1:]))
    ans += int(pieces * 9 <= l * r)

print(ans)
