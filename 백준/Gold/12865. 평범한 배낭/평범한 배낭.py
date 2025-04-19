# 12865. 평범한 배낭

N,K = map(int,input().split())
backpack = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]* (K+1) for _ in range(N+1)]
for i in range(K+1):
    for j in range(1,N+1):
        if backpack[j-1][0] <= i:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i - backpack[j-1][0]] + backpack[j-1][1])
        else:
            dp[j][i] = dp[j-1][i]

print(dp[-1][-1])