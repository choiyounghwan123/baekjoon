# 2566. 최대값

matrix = []

for _ in range(9):
    matrix.append(list(map(int,input().split())))

max_ = -1
i_,j_ = 0,0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_:
            max_ = matrix[i][j]
            i_,j_ = i,j

print(max_)
print(i_+1,j_+1)