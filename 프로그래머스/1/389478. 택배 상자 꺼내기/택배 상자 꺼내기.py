# [2025 프로그래머스 코드챌린지 2차 예선]

def solution(n, w, num):
    boxs = [[] for _ in range(w)]
    i,j,k = 0,0,1

    while k <= n:
        if k % w == 0:
            j+=1
            boxs[i].append(k)
            k+=1
            continue
        boxs[i].append(k)
        k+=1
        if j % 2 == 0:
            i+=1
        else:
            i-=1
    result = 1
    for box in boxs:
        if num in box:
            while box[-1] != num:
                box.pop(-1)
                result += 1
            break
    return result

print(solution(22,6,8))