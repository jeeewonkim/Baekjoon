import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []
def back(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(start,n):
        ans.append(num[i])
        back(i+1)
        ans.pop()
back(0)

# for i in range(1,n+1):
#     for combi in combinations(num, i):
#         if sum(combi) == s:
#             cnt+=1

print(cnt)