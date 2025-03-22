# 15990. 1,2,3 더하기 5
import sys
N = int(sys.stdin.readline())
# 3 1+2 2+1 3

dp = []
dp.append([0,0,0])
dp.append([1,0,0])
dp.append([0,1,0])
dp.append([1,1,1])
for i in range(4, 100000+1):
    dp.append([(dp[i-1][1] + dp[i-1][2]) % 1000000009,(dp[i - 2][0] + dp[i - 2][2]) % 1000000009,(dp[i - 3][0] + dp[i - 3][1]) % 1000000009])
for _ in range(N):
    target = int(sys.stdin.readline())
    print(sum(dp[target]) % 1000000009)