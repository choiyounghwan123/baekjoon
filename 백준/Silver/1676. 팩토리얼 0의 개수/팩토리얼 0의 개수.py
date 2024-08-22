# 팩토리얼 0의 개수
import math
import sys
N = int(sys.stdin.readline())
factorial = list(str(math.factorial(N)))
res = 0
for i in range(len(factorial)-1,-1,-1):
    if factorial[i] != '0':
        break
    res+=1
print(res)