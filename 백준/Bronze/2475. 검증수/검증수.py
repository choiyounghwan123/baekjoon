import sys

nums = list(map(int,sys.stdin.readline().split()))

res = 0

for i in nums:
    res += i**2
print(res%10)