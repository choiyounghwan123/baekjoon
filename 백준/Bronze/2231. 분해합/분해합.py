import sys

N = int(sys.stdin.readline())

result = 0

for i in range(N):
    temp = list(str(i))
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    if i + sum(temp) == N:
        result = i
        break
print(result)
