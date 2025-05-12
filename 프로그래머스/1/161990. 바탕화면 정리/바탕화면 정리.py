# 프로그래머스 LV1. 바탕화면 정리

def solution(wallpaper):
    x1,x2,y1,y2 = 0,0,0,0
    flag = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x1 = i
                flag = 1
                break
        if flag:
            break
    flag = 0
    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":
                x2 = i
                flag = 1
                break
        if flag:
            break
    flag = 0
    for i in range(len(wallpaper)-1,-1,-1):
        for j in range(len(wallpaper[i])-1,-1,-1):
            if wallpaper[i][j] == '#':
                y1 = i
                flag = 1
                break
        if flag:
            break
    flag = 0
    for i in range(len(wallpaper[0])-1,-1,-1):
        for j in range(len(wallpaper)-1,-1,-1):
            if wallpaper[j][i] == "#":
                y2 = i
                flag = 1
                break
        if flag:
            break
    return [x1,x2,y1+1,y2+1]



