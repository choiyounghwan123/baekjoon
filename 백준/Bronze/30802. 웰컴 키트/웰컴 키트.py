import sys

N = int(sys.stdin.readline())
sizes = list(map(int,sys.stdin.readline().split()))
T,P = map(int,sys.stdin.readline().split())

result = 0

for i in range(6):
    if sizes[i]%T == 0:
        result += sizes[i] // T
    else:
        result += sizes[i]//T + 1
print(result)
print(N//P,N%P)