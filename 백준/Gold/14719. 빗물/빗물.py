
    #
#aa##
#a###aa#
########
########

# 14719. 빗물

H,W = map(int,input().split())
height = list(map(int,input().split()))

result = 0

for i in range(1,W-1):
    temp = min(max(height[:i]),max(height[i+1:])) - height[i]
    if  temp < 0:
        continue
    result += temp
print(result)


