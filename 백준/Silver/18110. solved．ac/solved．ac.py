# solved.ac
import math
import sys


def rounds(x):
    if x - math.floor(x) >= 0.5:
        return math.ceil(x)
    else:
        return math.floor(x)


N = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(N)]

d = rounds(N * 0.15)
score.sort()
if N -d -d <= 0:
    print(0)
else:
    print(rounds(sum(score[d:N-d]) / (N - d - d)))
