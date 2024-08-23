# 오븐 시계

import sys

A,B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())

B += C

if B >=60:
    A += B // 60
    B %= 60

if A >= 24:
    A-=24

print(A,B)