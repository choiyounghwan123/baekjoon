# 11722. 가장 긴 감소하는 부분 수열

N = int(input())
A = list(map(int,input().split()))

dp = [1] * (N+1)

for i in range(N):
    for j in range(i,N):
        if A[i] > A[j]:
            dp[j] = max(dp[j],dp[i] + 1)

print(max(dp))
