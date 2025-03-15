# 2110. 공유기 설치

N,C = map(int,input().split())

x = []

for _ in range(N):
    x.append(int(input()))
x.sort()
start,end = 1, x[-1]-x[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    cur = 1
    cnt = x[0]

    for i in range(1,N):
        if x[i] - cnt >= mid:
            cur += 1
            cnt = x[i]
    if cur >= C:
        start = mid + 1
        result = max(result,mid)
    else:
        end = mid - 1
print(result)