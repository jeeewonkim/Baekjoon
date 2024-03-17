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
# for c in computer:
#     print(c)
#
# result = 0
# def bfs(x,y):
#     #global result
#     computer[x][y]  = 1
#     if x < 0 or x >= c_num or y < 0 or y>=c_num:
#         return False
#     if computer[x][y] and computer[y][x]:
#         computer[x][y],computer[y][x] = False,False
#         bfs(x-1,y)
#         bfs(x+1,y)
#         bfs(x,y-1)
#         bfs(x,y+1)
#         return True
#     return False
#
# for x in range(c_num):
#     for y in range(c_num):
#         if bfs(x,y):
#             result +=1



