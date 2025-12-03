import sys
s = 0
for line in sys.stdin:
    line = line.strip()
    n = len(line)
    highest = float('-inf')
    for i in range(n-1):
        for j in range(i+1,n):
            num = int(line[i] + line[j])
            highest = max(highest, num)

    s += highest

print(s)