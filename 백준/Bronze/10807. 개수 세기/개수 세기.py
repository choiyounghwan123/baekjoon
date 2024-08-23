# 개수 세기

import sys

T = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())
print(nums.count(v))