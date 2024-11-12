# 2748. 피보나치 수 2

fibonacci = [0,1]

n = int(input())

for i in range(2,n+1):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

print(fibonacci[n])