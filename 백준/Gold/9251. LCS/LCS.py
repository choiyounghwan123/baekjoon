# 9251. LCS


"""
input: ACAYKP
input: CAPCAK
output: 4
"""

A = input()
B = input()
dp = [[0] * (len(A) + 1) for _ in range(len(B)+1)]
for i in range(1,len(A)+1):
    dp[0][i] = 0
for i in range(1,len(B)+1):
    dp[i][0] = 0

for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        if A[j-1] == B[i-1]:
            dp[i][j]  = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
