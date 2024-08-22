# IOIOI

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i + 3] == "IOI":
        count += 1
        i += 2

        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
