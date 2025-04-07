# 13305. 주유소
from operator import length_hint

N = int(input())
length = list(map(int,input().split()))
costs = list(map(int,input().split()))

min_ = 1000000000
result = 0
a = 0
for i in range(N-1):
    if min_ > costs[i]:
        result += min_ * a
        min_ = costs[i]
        a = length[i]
    else:
        a += length[i]


print(result + a * min_)

