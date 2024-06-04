import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dict = {}
for a in num:
    if a not in dict.keys():
        dict[a] = 1
    else:
        dict[a]+=1

stack = []
answer = [-1 for _ in range(n)]

for i in range(n):
    while stack and dict[num[stack[-1]]] < dict[num[i]]:
        answer[stack.pop()] = num[i]
    stack.append(i)

print(*answer, end = " ")