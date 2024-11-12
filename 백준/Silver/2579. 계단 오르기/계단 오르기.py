# 2579. 계단 오르기

n = int(input())
stairs = [0]
for i in range(n):
    stairs.append(int(input()))

dp = [0] * 301
if n == 1:
    print(stairs[1])
    exit()
elif n == 2:
    print(stairs[1] + stairs[2])
    exit()
dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]


for i in range(3,n+1):
    dp[i] = max(dp[i-2] , dp[i-3] +stairs[i-1]) + stairs[i]


print(dp[n])
