import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    for j in range(i):
        print("*",end="")
    print()