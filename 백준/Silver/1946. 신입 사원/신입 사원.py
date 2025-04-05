# 1946. 신입 사원

import sys

for _ in range(int(sys.stdin.readline())):
    applicantCount = int(sys.stdin.readline())
    scores = [list(map(int, sys.stdin.readline().split())) for _ in range(applicantCount)]
    scores.sort()
    result = 1
    top = 0
    for i in range(1,applicantCount):
        if scores[i][1] < scores[top][1]:
            result += 1
            top = i
    print(result)



