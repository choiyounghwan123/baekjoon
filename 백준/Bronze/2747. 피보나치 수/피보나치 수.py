# 2747. 피보나치 수

n = int(input())

dp = [0] * (n+1)

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(1)
    exit()

dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])