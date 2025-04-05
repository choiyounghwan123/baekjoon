# 18185. 라면 사기(Small)

N = int(input())
noodles = list(map(int,input().split()))
result = 0

i = 0

while i < N:
    if noodles[i] == 0:
        i+=1
        continue
    elif i < N -2 and noodles[i+1] > noodles[i+2]:
        result += 5
        noodles[i] -= 1
        noodles[i+1] -= 1
    elif i < N - 2 and noodles[i] > 0 and noodles[i+1] > 0 and noodles[i+2] > 0:
        noodles[i] -= 1
        noodles[i+1] -= 1
        noodles[i+2] -= 1
        result += 7
    elif i < N - 1 and noodles[i] > 0 and noodles[i+1] > 0:
        noodles[i+1] -=1
        noodles[i] -= 1
        result+=5
    else:
        result+=3
        noodles[i] -= 1

print(result)

