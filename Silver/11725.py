import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
tree = {i : [] for i in range(1,n+1)}
parent = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
def find(start):
    q = deque()
    q.append(start)
    parent[start] = start
    while q:
        now = q.popleft()
        if now not in tree:

            continue
        for i in tree[now]:
            if parent[i] == 0:
                parent[i]  = now
                q.append(i)
find(1)
for p in parent[2:]:
    print(p)

# def preorder(root):
#     if root !='.':
#         print(root, end = '')
#         preorder(tree[root][0])
#         preorder(tree[root][1])
#
# def inorder(root):
#     if root!='.':
#         inorder(tree[root][0])
#         print(root, end = "")
#         inorder(tree[root][1])
#
# def postorder(root):
#     if root!='.':
#         postorder(tree[root][0])
#         postorder(tree[root][1])
#         print(root, end = "")
#
#
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')