# 피보나치 함수

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    dp1 = [0] * (N + 1)
    dp2 = [0] * (N + 1)
    if N == 0:
        print("1 0")
        continue
    elif N == 1:
        print("0 1")
        continue
    dp1[0] = 1
    dp1[1] = 0
    dp2[0] = 0
    dp2[1] = 1

    for i in range(2, N + 1):
        dp1[i] = dp1[i - 1] + dp1[i - 2]
        dp2[i] = dp2[i - 1] + dp2[i - 2]
    print(dp1[N], dp2[N])
