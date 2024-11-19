# 2460. 지능형 기차2
result = 0
current = 0
for _ in range(10):
    exitCount, enterCount = map(int,input().split())
    current =  current - exitCount + enterCount
    result = max(result, current)
print(result)
