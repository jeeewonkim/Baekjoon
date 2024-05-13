import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
num = [i for i in range(9,-1,-1)]
op = list(map(str, input().split()))
result = []
answer = []
visited = [False] * (10)

def back(cnt, result, li):
    if cnt == n+1:
        answer.append(result[:])
        return

    for i in range(10):
        if not result:
            result.append(li[i])
            back(cnt+1, result,li)
            result.pop()
        elif result and li[i] not in result:
            if op[len(result)-1] == '<':
                if result[-1] < li[i]:
                    result.append(li[i])
                    back(cnt+1, result,li)
                    result.pop()
            elif op[len(result)-1] == '>':
                if result[-1] > li[i]:
                    result.append(li[i])
                    back(cnt+1, result,li)
                    result.pop()

back(0, result,num)
print(''.join(map(str, answer[0])))
print(''.join(map(str, answer[-1])))