# 상수

import sys

a,b = map(str,sys.stdin.readline().split())
print(max(int("".join(reversed(a))),int("".join(reversed(b)))))