# 1789. 수들의 합

S = int(input())

start, end = 1, S
answer = 0
while start <= end:
    mid = (start + end) // 2
    if mid * (mid+1) // 2 <= S:
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)
