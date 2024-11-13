# 10798. 세로 읽기

str_list = []

for _ in range(5):
    str_list.append(input().rstrip())

for i in range(15):
    for j in range(6):
        try:
            print(str_list[j][i], end="")
        except:
            continue
