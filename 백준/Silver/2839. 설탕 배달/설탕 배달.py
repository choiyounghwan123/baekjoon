# 설탕 배달

import sys

N = int(sys.stdin.readline())

if N % 5 == 0:
    print(N//5)
else:
    p = 0

    while N > 0 :
        N-=3
        p+=1

        if N % 5 == 0:
            print(p+N//5)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(p)
            break
