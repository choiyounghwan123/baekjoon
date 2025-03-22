# 16194. 카드 구매하기 2

N = int(input())
P = list(map(int,input().split()))
P.insert(0,0)
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i] = P[i]
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j] + P[j])

print(dp[N])
