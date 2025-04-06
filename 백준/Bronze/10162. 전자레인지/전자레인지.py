# 10162. 전자레인지

T = int(input())
result = [0,0,0]

if T % 10 != 0:
    print(-1)
    exit()

while T != 0:
    if T >= 300:
        T-=300
        result[0] +=1
    elif T >= 60:
        T -= 60
        result[1] += 1
    else:
        T -= 10
        result[2] += 1
print(*result)

