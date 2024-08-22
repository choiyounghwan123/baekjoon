import sys

hour, minute = map(int,sys.stdin.readline().split())

for i in range(1,46):
    if minute == 0:
        if hour == 0:
            hour = 23
        else:
            hour-=1
        minute = 60
    minute-=1

print(hour,minute)