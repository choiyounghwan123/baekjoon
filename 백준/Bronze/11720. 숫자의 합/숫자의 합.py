# 숫자의 합 구하기

import sys
N = int(sys.stdin.readline())
nums = list(sys.stdin.readline().strip())
sum = 0

for num in nums:
    sum += int(num)
print(sum)