# 1991. 트리 순회

N = int(input())
tree = dict()

for _ in range(N):
    root, left_child, right_child = map(str, input().strip().split())
    tree[root] = [left_child, right_child]


def predorder(root):
    print(root, end="")
    if tree[root][0] != '.':
        predorder(tree[root][0])
    if tree[root][1] != '.':
        predorder(tree[root][1])


def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end="")
    if tree[root][1] != '.':
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end="")


predorder("A")
print()
inorder("A")
print()
postorder("A")