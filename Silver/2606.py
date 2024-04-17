#바이러스
import sys

input = sys.stdin.readline
from collections import deque

count = 0
c_num = int(input())
loop = int(input())
computer = [[False] * (c_num + 1) for _ in range(c_num + 1)]

for i in range(loop):
    a, b = map(int, input().split())
    computer[a][b], computer[b][a] = True, True
visited = [False] * (c_num + 1)


def virus(computer, start):
    global count
    visited[start] = True
    queue = deque([start])
    while queue:
        x = queue.popleft()
        count += 1
        for i in range(1, c_num + 1):
            if not visited[i] and computer[x][i]:
                visited[i] = True
                queue.append(i)


virus(computer, 1)
print(count - 1)


#깊이 우선 탐색

import sys
input = sys.stdin.readline

c_num = int(input())
net = int(input())



computer = [[]*(c_num+1) for _ in range(c_num+1)]
for i in range(net):
    a,b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

visited = [0]*(c_num+1)

cnt =0

def dfs(virus):
    global cnt
    visited[virus] = 1
    for i in computer[virus]:
        if (visited[i] == 0):
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)



#바이러스
import sys

input = sys.stdin.readline
from collections import deque

count = 0
c_num = int(input())
loop = int(input())
computer = [[False] * (c_num + 1) for _ in range(c_num + 1)]

for i in range(loop):
    a, b = map(int, input().split())
    computer[a][b], computer[b][a] = True, True
visited = [False] * (c_num + 1)


def virus(computer, start):
    global count
    visited[start] = True
    queue = deque([start])
    while queue:
        x = queue.popleft()
        count += 1
        for i in range(1, c_num + 1):
            if not visited[i] and computer[x][i]:
                visited[i] = True
                queue.append(i)


virus(computer, 1)
print(count - 1)
