# 팰린드롬인지 확인하기

import sys

palindrome = sys.stdin.readline().rstrip()

left,right = 0, len(palindrome) - 1

while left < right:
    if palindrome[left] != palindrome[right]:
        print(0)
        break
    left+=1
    right-=1
else:
    print(1)