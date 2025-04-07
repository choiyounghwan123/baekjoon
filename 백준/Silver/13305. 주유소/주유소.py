# 13305. 주유소

N = int(input())
length = list(map(int,input().split()))
costs = list(map(int,input().split()))
min_ = 1000000
result = 0
a = 0
for i in range(N-2,-1,-1):
    if costs[i] >= min_:
        result += a * min_
        min_ = costs[i]
        a = length[i]
    else:
        min_ = costs[i]
        a+=length[i]
if a:
    result += a * min_

print(result)
