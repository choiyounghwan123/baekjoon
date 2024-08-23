# 문자열

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    word = sys.stdin.readline().rstrip()
    print(f"{word[0]}{word[-1]}")