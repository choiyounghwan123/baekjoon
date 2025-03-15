# 1790. 수 이어 쓰기 2

N,K = map(int,input().split())

start = 0
digit = 1
nine = 9

while K > nine * digit:
    K = K - nine * digit
    start = start + nine
    nine *= 10
    digit += 1

result = (start + 1) + (K-1)//digit

if result > N:
    print(-1)
else:
    print(str(result)[(K-1)%digit])

