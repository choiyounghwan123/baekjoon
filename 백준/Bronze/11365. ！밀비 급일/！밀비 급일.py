# 11365. !밀비 급일
import sys
command = sys.stdin.readline().rstrip()

while command != "END":
    print(command[::-1])
    command = sys.stdin.readline().rstrip()
