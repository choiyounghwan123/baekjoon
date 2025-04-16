# 4016. 수열의 연속 합

N,M = map(int,input().split())
nums = list(map(int,input().split()))

hash_map = dict()
hash_map[0] = 1
sum_ = 0
count = 0
for i in range(N):
    sum_ += nums[i]

    if sum_ - M in hash_map:
        count += hash_map[sum_ - M]
    hash_map[sum_] = hash_map.get(sum_,0) + 1
print(count)