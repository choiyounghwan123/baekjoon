# 통계학

import sys
import math


def rounds(x):
    if x - math.floor(x) >= 0.5:
        return math.ceil(x)
    else:
        return math.floor(x)


N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))
print(rounds(sum(nums) / N))
nums.sort()
print(nums[N // 2])
my_list = [[0, i] for i in range(0, 8001)]

for i in range(N):
    a = 4000 + nums[i]
    my_list[a] = [my_list[a][0] + 1, my_list[a][1]]
my_list.sort(key=lambda k: (k[0],-k[1]))

if my_list[-2][0] == my_list[-1][0]:
    print(my_list[-2][1]-4000)
else:
    print(my_list[-1][1]-4000)

print(max(nums) - min(nums))
