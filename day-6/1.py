import sys
numbers = []
for line in sys.stdin:
    line = line.strip()
    try:
        numbers.append(list(map(int, line.split())))
    except ValueError:
        numbers.append(line.split())

ops = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b
}

from functools import reduce
total = 0
for c in range(len(numbers[-1])):
    op = ops[numbers[-1][c]]
    ans = reduce(op, [ numbers[r][c] for r in range(len(numbers)-1) ])
    total += ans

print(total)