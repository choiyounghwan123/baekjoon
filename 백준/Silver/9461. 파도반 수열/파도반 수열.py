# 파도반 수열

import sys

for _ in range(int(sys.stdin.readline())):
    dp = [0] * 101
    dp[1] = dp[2] = dp[3] = 1

    N = int(sys.stdin.readline())

    for i in range(4,N+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])