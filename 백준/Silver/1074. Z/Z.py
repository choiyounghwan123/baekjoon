# Z

import sys
sys.setrecursionlimit(10**6)

N, r, c = map(int, sys.stdin.readline().split())
cnt = 0

def recursion(n,x,y):
    global cnt

    if n == 0:
        if x == c and y == r:
            print(cnt)
        cnt += 1
        return

    half = 2 ** (n-1)

    if c < x + half and r < y + half:
        recursion(n-1,x,y)
    else:
        cnt += half * half

    if c >= x+half and r < y + half:
        recursion(n-1,x+half,y)
    else:
        cnt += half * half

    if c < x + half and r >= y + half:
        recursion(n-1,x,y+half)
    else:
        cnt += half * half

    if c >= x+half and r >= y+half:
        recursion(n-1,x+half,y+half)
    else:
        cnt += half * half


recursion(N,0,0)