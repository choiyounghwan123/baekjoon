# 1699. 제곱수의 합

N = int(input())
dp = [1000001] * (N+5)
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1

for i in range(2,int(N**0.5)+1):
    dp[i ** 2] = 1

for i in range(5,N+1):
    for j in range(1, int(i ** 0.5)+1):
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])

print(dp[N])