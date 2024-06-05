import sys
input = sys.stdin.readline

n = int(input())
stack = []
score = 0
for _ in range(n):

    a = list(map(int, input().split()))

    if a[0] == 1:
        if a[2]-1 == 0:
            score += a[1]
        else:
            stack.append([a[1],a[2]-1])

    else:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                score += stack.pop()[0]
print(score)