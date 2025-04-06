# 3109. 빵집

N,M = map(int,input().split())
A = [list(map(int,input().strip())) for _ in range(N)]
B = [list(map(int,input().strip())) for _ in range(N)]
if A == B:
    print(0)
    exit()
def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j] = 1 - A[i][j]

result = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            result+=1
            flip(i,j)
        if A == B:
            print(result)
            exit()
else:
    print(-1)