# 2096. 내려가기

from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
dp1 =  arr
dp2 = arr

for _ in range(N - 1):
    arr = list(map(int, stdin.readline().split()))
    dp1 = [arr[0] + max(dp1[0], dp1[1]), arr[1] + max(dp1), arr[2] + max(dp1[1], dp1[2])]
    dp2 = [arr[0] + min(dp2[0], dp2[1]), arr[1] + min(dp2), arr[2] + min(dp2[1], dp2[2])]

print(max(dp1), min(dp2))
