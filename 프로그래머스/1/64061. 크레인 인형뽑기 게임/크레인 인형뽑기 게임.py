# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# [2019 카카오 개발자 겨울 인턴십] 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if stack and stack[-1] == board[i][move-1]:
                    answer += 2
                    stack.pop(-1)
                    board[i][move-1] = 0
                    break
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    print(stack)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))