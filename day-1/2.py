import sys
current = 50
ans = 0

def f(p,t,dir):
    if t == 0: return 0
    if p == 0:
        return abs(t) // 100
    elif dir == 'L':
        next_position = max(p-t, 0) % 100
        return (next_position == 0) + f(next_position, t - min(p,t), 'L')
    else:
        next_position = min(p+t, 100) % 100
        return (next_position == 0) + f(next_position, t - min(100 - p, t), 'R')

for line in sys.stdin:
    line = line.strip()

    direction = line[0]
    amount = int(line[1:])

    ans += f(current, amount, direction)
    if direction == 'L': amount *= -1
    current = (current + amount) % 100

print(ans)
