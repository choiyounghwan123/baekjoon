# 9019. DSLR

from collections import deque

for _ in range(int(input())):
    A,B = map(int,input().split())
    queue = deque([[A,""]])
    visited = [False] * 100001
    while queue:
        num, path = queue.popleft()

        if num == B:
            print(path)
            break


        D = (2 * num) % 10000
        if not visited[D]:
            queue.append([D,path + "D"])
            visited[D] = True
        S = (num-1) % 10000
        if not visited[S]:
            queue.append([S,path + "S"])
            visited[S] = True

        L = (10*num+(num//1000))%10000
        if not visited[L]:
            queue.append(([L, path + "L"]))
            visited[L] = True
            
        R = (num//10+(num%10)*1000)%10000
        if not visited[R]:
            queue.append([R, path + "R"])
            visited[R] = True