import sys

for _ in range(int(sys.stdin.readline())):
    result = list(sys.stdin.readline())
    score = 0
    check = 0
    for i in result:
        if i == 'O':
            if check == 0:
                score += 1
                check = 1
            else:
                check+=1
                score+=check
        else:
            check=0
    print(score)

