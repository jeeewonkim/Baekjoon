import sys
input = sys.stdin.readline

n = int(input())
stack =[]
ans = []
res = []
start = 1

for _ in range(n):
    ans = int(input())

    while start <= ans:
        stack.append(start)
        start +=1
        res.append('+')

    if ans == stack[-1]:
        p = stack.pop()
        res.append('-')

    else:
        res = ['NO']
        break

for i in res:
    print(i)