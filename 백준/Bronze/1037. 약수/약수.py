# 1037. 약수


N = int(input())
nums = sorted(list(map(int,input().split())))

print(max(nums) * min(nums))

