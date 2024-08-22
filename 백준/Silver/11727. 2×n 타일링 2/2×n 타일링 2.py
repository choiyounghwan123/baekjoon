# 2xn 타일링 2

import sys

N = int(sys.stdin.readline())
dp = [0] * 1001
dp[1],dp[2],dp[3] = 1,3,5

for i in range(4,N+1):
    dp[i] = dp[i-2] *2 + dp[i-1]

print(dp[N]%10007)