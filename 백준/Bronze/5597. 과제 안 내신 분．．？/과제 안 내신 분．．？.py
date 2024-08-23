# 과제 안 내신 분..?

import sys

students = [0] * 30

for _ in range(28):
    n = int(sys.stdin.readline())
    students[n-1] = 1

for idx,student in enumerate(students):
    if student == 0:
        print(idx+1)