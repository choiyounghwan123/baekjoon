# 잃어버린 괄호

import sys

s = sys.stdin.readline().rstrip().split("-")
res = 0
if len(s) == 1:
    s = str(s[0]).split("+")
    for i in s:
        res+=int(i)
else:
    for i in s[0].split("+"):
        res+=int(i)

    for i in range(1,len(s)):
        temp_str = s[i].split("+")

        for j in temp_str:
            res-=int(j)

print(res)
