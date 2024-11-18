# 3460. 이진수

for _ in range(int(input())):
    decimal_ = int(input())
    binary_number = []
    i = 0
    while decimal_ != 0:
        if decimal_%2 == 1:
            print(i, end=" ")
        decimal_ = decimal_//2
        i+=1
    print()
