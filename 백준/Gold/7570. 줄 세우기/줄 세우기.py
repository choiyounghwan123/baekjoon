# 1078. 줄 세우기

N = int(input())
nums = list(map(int,input().split()))

dp = [0] * (N+1)

for i in range(N):
    dp[nums[i]] = dp[nums[i] - 1] + 1
print(N - max(dp))