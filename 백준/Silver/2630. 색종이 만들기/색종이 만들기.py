# 색종이 만들기

import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

white_paper = 0 # 0
blue_paper = 0 # 1

def slice(x,y,n):
    tmp = paper[y][x]
    global white_paper,blue_paper
    for i in range(y,y+n):
        for j in range(x,x+n):
            if tmp != paper[i][j]:
                slice(x,y,n//2)
                slice(x+n//2,y,n//2)
                slice(x,y+n//2,n//2)
                slice(x+n//2,y+n//2,n//2)
                return
    else:
        if tmp == 0:
            white_paper+=1
        else:
            blue_paper+=1



slice(0,0,N)

print(white_paper)
print(blue_paper)