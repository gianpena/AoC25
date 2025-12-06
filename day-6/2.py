import sys
numbers = []
for line in sys.stdin:
    line = line[:-1]
    if not line: break
    numbers.append(line)

column_lengths = []
i = 0
current = 0
while i < len(numbers[-1]):
    if numbers[-1][i] in '+*':
        column_lengths.append(current)
        current = 0
    else:
        current += 1
    i += 1

column_lengths.append(current+1)
column_lengths = column_lengths[1:]

total = 0
for c in range(len(column_lengths)):
    column_start = sum(column_lengths[:c]) + c

    op = numbers[-1][column_start]
    ans = 0 if op == '+' else 1
    for i in range(column_start + column_lengths[c]-1, column_start-1, -1):
        number = ''.join( [numbers[r][i] if numbers[r][i] else '' for r in range(len(numbers)-1)] )
        if op == '+':
            ans += int(number)
        else:
            ans *= int(number)

    total += ans

print(total)