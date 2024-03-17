import sys

input = sys.stdin.readline

n = int(input())
start = 1
support = 2
goal = 3
answer = []
def hanoi(n,start, goal, support):
    if n == 1:
        answer.append([start,goal])
    else:
        hanoi(n - 1, start, support, goal)
        hanoi(n-1, start, goal, support)
        hanoi(n-1,support, goal ,start)

hanoi(n,1,3,2)
print(answer)
#     n = int(input())
#     if n == 1:
#
#     answer = [[]]
#     return answer