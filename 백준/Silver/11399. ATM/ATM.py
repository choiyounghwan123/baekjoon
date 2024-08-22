# ATM

import sys

N = int(sys.stdin.readline())
times = sorted(list(map(int,sys.stdin.readline().split())))
res = 0
dp = [0] * (N+1)
dp[1] = times[0]

for i in range(2,N+1):
    dp[i] = dp[i-1] + times[i-1]

print(sum(dp))