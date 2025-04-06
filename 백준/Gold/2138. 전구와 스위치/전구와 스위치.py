# 2138. 전구와 스위치

N = int(input())
a = list(map(int,input().strip()))
a_ = a.copy()
b = list(map(int,input().strip()))
if a == b:
    print(0)
    exit()
a[0],a[1] = 1 - a[0], 1-a[1]
result1 = 1
for i in range(1,N):
    if a[i-1] != b[i-1] and i < N -1:
        result1+=1
        a[i-1],a[i],a[i+1] = 1 - a[i-1], 1 - a[i], 1-a[i+1]
    elif a[i-1] != b[i-1] and i == N-1:
        result1+=1
        a[i-1],a[i] = 1 - a[i-1], 1-a[i]
# if a == b:
#     print(result1)
#     exit()
result = 0
for i in range(1,N):
    if a_[i-1] != b[i-1] and i < N -1:
        result+=1
        a_[i-1],a_[i],a_[i+1] = 1 - a_[i-1], 1 - a_[i], 1-a_[i+1]
    elif a_[i-1] != b[i-1] and i == N-1:
        result+=1
        a_[i-1],a_[i] = 1 - a_[i-1], 1-a_[i]
if a_==b and a == b:
    print(min(result,result1))
elif a_==b:
    print(result)
elif a == b:
    print(result1)
else:
    print(-1)