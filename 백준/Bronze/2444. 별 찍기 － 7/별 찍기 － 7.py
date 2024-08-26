# 별 찍기 - 7

import sys

N = int(sys.stdin.readline())
k = 1
for i in range(N*2):
    if i < N:
        for j in range(N-i,1,-1):
            print(end =" ")
        print("*"*k)
        k += 2
    elif i == N:
        k-=2
    else:
        for j in range(i-N+1,1,-1):
            print(end=" ")
        k-=2
        print("*"*k)
