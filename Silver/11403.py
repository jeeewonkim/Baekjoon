import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [[] for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]
for num in range(n):
    m = list(map(int, input().split()))
    for i in range(n):
        if m[i] == 1:
            matrix[num].append(i)
def solve(start):
    q = deque([start])
    visited = [False]*n
    while q:
        now = q.popleft()
        for i in matrix[now]:
            if not visited[i]:
                result[start][i]=1
                visited[i] = True
                q.append(i)

for i in range(n):
    solve(i)
for r in result:
    print(*r)