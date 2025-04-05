# 22864. 피로도

A,B,C,D = map(int,input().split())
fatigue = 0
result = 0
for i in range(1,25):
    if fatigue + A > D:
        fatigue = max(0, fatigue - C)
    else:
        result += B
        fatigue += A
print(result)