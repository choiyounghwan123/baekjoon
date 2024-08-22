# FizzBuzz
import sys

s = list(sys.stdin.readline().rstrip() for _ in range(3))
temp = 0
check = 1
for i in range(3):
    if s[i] != 'Fizz' and s[i] != 'Buzz' and s[i] != 'FizzBuzz':
        temp = int(s[i]) + (3-i)
        check = 0
if check:
    print("Buzz")

if temp % 3 == 0 and temp % 5 == 0:
    print("FizzBuzz")
elif temp % 3 ==0 and temp % 5 != 0:
    print("Fizz")
elif temp % 3 != 0 and temp % 5 == 0:
    print("Buzz")
else:
    print(temp)
