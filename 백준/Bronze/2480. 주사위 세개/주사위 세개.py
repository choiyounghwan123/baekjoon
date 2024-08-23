# 주사위 세개

import sys

A,B,C = map(int,sys.stdin.readline().split())

if A == B:
    if B == C:
        print(10000+A*1000)
    else:
        print(1000+A*100)
elif A == C:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
else:
    print(max(A,B,C) * 100)