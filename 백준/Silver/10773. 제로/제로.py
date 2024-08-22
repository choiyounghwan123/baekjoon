# 제로

import sys
nums = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))
