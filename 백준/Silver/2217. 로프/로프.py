# 2217. 로프

import sys
input = sys.stdin.readline
n = int(input())
ropes = list(int(input()) for _ in range(n))
ropes.sort(reverse=True)
result = ropes[0]
for i in range(1,n):
    result = max(result, (i+1) * ropes[i])
print(result)