# 수 찾기

import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums_dict = dict()
for num in nums:
    nums_dict[num] = nums_dict.get(num,0) + 1

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

for num in nums:
    if nums_dict.get(num,0):
        print("1")
    else:
        print("0")
