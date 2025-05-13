# 9663. N-Queen
N = int(input())
board = [0] * N
ans = 0

def is_promising(n:int)->bool:
    for i in range(n):
        if board[i] == board[n] or abs(board[n] - board[i]) == abs(n-i):
            return False
    return True


def dfs(start):
    global ans
    if start == N:
        ans += 1
        return
    for i in range(N):
        board[start] = i
        if is_promising(start):
            dfs(start+1)
dfs(0)
print(ans)