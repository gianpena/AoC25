import sys
current = 50
zeroes = 0
for line in sys.stdin:
    line = line.strip()

    direction = line[0]
    amount = int(line[1:])
    if direction == 'L':
        current = (current - amount) % 100
    else:
        current = (current + amount) % 100


    zeroes += (current == 0)

print(zeroes)
