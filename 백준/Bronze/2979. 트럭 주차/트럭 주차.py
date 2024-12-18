# 2979. 트럭 주차


A,B,C = map(int,input().split())
price = [0] * 100

for i in range(3):
    start,end = map(int,input().split())
    for j in range(start,end):
        price[j] += 1

answer = 0

for i in range(100):
    if price[i] == 1:
        answer +=A
    elif price[i] == 2:
        answer += B * 2
    elif price[i] == 3:
        answer += C * 3
print(answer)