import sys
s = 0
for line in sys.stdin:
    line = line.strip()
    n = len(line)
    remaining = 12
    i = 0
    st = []
    while i < n:
        while st and line[i] > st[-1] and n-i > remaining:
            st.pop()
            remaining += 1

        if remaining > 0:
            st.append(line[i])
            remaining -= 1
        i += 1

    s += int(''.join(st))


print(s)