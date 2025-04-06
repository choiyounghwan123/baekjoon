# 14916. 거스름돈

n = int(input())
result = 0
flag = False
while n > 0:
    if n % 5 == 0:
        result += n // 5
        n = n % 5

    else:
        result+=1
        n-=2

if n < 0:
    print(-1)
    exit()
print(result)