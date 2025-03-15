# 11729. 하노이 탑 이동 순서

N = int(input())

def hanoi(num,from_,to,other):
    if num == 1:
        print(from_,to)
        return
    hanoi(num-1,from_,other,to)
    print(from_,to)
    hanoi(num-1, other,to,from_)

print(2**N-1)
hanoi(N,1,3,2)