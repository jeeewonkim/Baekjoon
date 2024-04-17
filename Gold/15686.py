import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split())
chicken = []
home = []
result = 999999
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 2:
            chicken.append([i,j])
        if city[j] == 1:
            home.append([i,j])
visited = [False] * (len(chicken))
# def back(idx, cnt):
#     global result
#
#     if cnt == m:
#         ans = 0
#
#     for i in home:
#         dist = 999999
#
#         for j in range(len(visited)):
#             if visited[j]:
#                 num_dist = abs(i[0]- chicken[j][0])+abs(i[1]-chicken[j][1])
#                 dist = min(num_dist, dist)
#             ans += dist
#         result = min(result, ans)
#
#         return
#
#     for i in range(idx,len(chicken)):
#         if not visited[i]:
#             visited[i] = True
#             back(i+1, cnt+1)
#             visited[i] = False
# back(0,0)
#
# print(result)

for chi in combinations(chicken, m):
    temp = 0
    for h in home:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-chi[j][0])+abs(h[1]-chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)