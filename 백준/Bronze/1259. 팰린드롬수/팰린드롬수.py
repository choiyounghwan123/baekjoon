import sys

while True:
    num = list(sys.stdin.readline().rstrip())

    if num[0] == '0':
        break

    left,right = 0,len(num) - 1
    check = 1
    while left < right:
        if int(num[left]) != int(num[right]):
            print("no")
            check = 0
            break
        left+=1
        right-=1
    if check:
        print("yes")
