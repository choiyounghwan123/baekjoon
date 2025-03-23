# 1912. 연속합

N = int(input())
nums = list(map(int, input().split()))
dp = [-1001] * (N+1)

for i in range(1,N+1):
    dp[i] = max(dp[i], nums[i-1],dp[i-1] + nums[i-1])
print(max(dp))