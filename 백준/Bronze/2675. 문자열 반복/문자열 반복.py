import sys

N = int(sys.stdin.readline())

for _ in range(N):
    r, s = map(str, sys.stdin.readline().split())
    s = list(s)
    for i in s:
        print(i*int(r),end="")
    print()
