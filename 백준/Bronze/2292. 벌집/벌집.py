import sys

N = int(sys.stdin.readline())
i = 1
while N > 1:
    N = N - 6*i
    i+=1
print(i)