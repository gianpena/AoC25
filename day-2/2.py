from collections import Counter
import sys
import re

IDs = input().split(',')

def invalid(ID):
    return re.fullmatch(r"([0-9]+)(?:\1)+", ID)

def sum_valid(a,b):
    ans = 0
    for i in range(a,b+1):
        if invalid(str(i)):
            ans += i
    return ans

ans = 0
for i in range(len(IDs)):
    ID1, ID2 = map(int, IDs[i].split('-'))
    not_valid = sum_valid(ID1, ID2)
    ans += not_valid

print(ans)