# 11052. 카드 구매하기

N = int(input())
P = list(map(int,input().split()))
dp = [0 for i in range(N+1)]
P.insert(0,0)

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[N])

