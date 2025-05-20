# [2025 프로그래머스 코드챌린지 1차 예선] 지게차와 크레인

def fork_list(request,storage):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    index = list()
    for i in range(1,len(storage)-1):
        for j in range(1,len(storage[0])-1):
            if storage[i][j] == request:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < len(storage) and 0 <= y < len(storage[x]) and storage[x][y] == "1":
                        index.append([i,j])
                        break

    for i in range(len(index)):
        storage[index[i][0]][index[i][1]] = "0"
        isOutSide(index[i][0],index[i][1],storage)


def crane(request,storage):
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == list(request)[0]:
                storage[i][j] = "0"
                isOutSide(i,j,storage)

def isOutSide(i,j,storage):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    outSide = False

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < len(storage) and 0 <= y < len(storage[x]) and storage[x][y] == "1":
            outSide = True
            storage[i][j] = "1"
            break

    if outSide:
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < len(storage) and 0 <= y < len(storage[x]) and storage[x][y] == "0":
                isOutSide(x,y,storage)


def solution(storage, requests):
    storage = [list("1" + s + "1") for s in storage]
    storage.insert(0, list("1" * len(storage[0])))
    storage.append(list("1" * len(storage[0])))



    for request in requests:
        if len(request) == 1:
            fork_list(request,storage)
        else:
            crane(request,storage)
    result = 0

    for i in range(1,len(storage)-1):
        for j in range(1, len(storage[i])-1):
            if storage[i][j] not in ("0","1"):
                result += 1
    return result
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"],["A", "BB", "A"]))