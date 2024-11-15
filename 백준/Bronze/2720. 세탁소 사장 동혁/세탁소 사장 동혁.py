# 2720. 세탁소 사장 동혁

for _ in range(int(input())):
    change = int(input())
    coins = [0,0,0,0]

    coins[0] = change // 25
    change %= 25
    coins[1] = change// 10
    change%=10
    coins[2] = change // 5
    change%=5
    coins[3] = change
    for i in range(4):
        print(coins[i], end=" ")
    print()