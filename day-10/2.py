import sys
import pulp as pl

indicators = []
buttons = []
joltage = []

for line in sys.stdin:
    line = line.strip()
    line = line.split()

    bits = line[0][1:-1].replace('.', '0').replace('#', '1')
    bits = int(bits, 2)
    indicators.append((bits, len(line[0])-2))

    buttons.append([])

    for i in range(1, len(line)-1):
        buttons[-1].append(list(map(int, line[i][1:-1].split(','))))
    joltage.append(tuple(map(int, line[-1][1:-1].split(','))))

from heapq import heappush, heappop
def shortest(i):

    prob = pl.LpProblem("min_sum", pl.LpMinimize)

    x = [pl.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(len(buttons[i]))]

    for j in range(len(joltage[i])):
        lhs = 0
        for k in range(len(buttons[i])):
            lhs = lhs + int(j in buttons[i][k]) * x[k]

        prob += lhs == joltage[i][j], f"eq_{j}"

    total = 0
    for j in range(len(buttons[i])):
        total = total + x[j]
    prob += total, "minimize_sum"

    prob.solve(pl.PULP_CBC_CMD(msg=0))

    ans = 0
    for j in range(len(buttons[i])):
        ans  += x[j].value()

    return ans

ans = 0
for i in range(len(joltage)):
    ans += shortest(i)

print(ans)