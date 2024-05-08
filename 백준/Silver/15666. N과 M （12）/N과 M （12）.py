import sys
from collections import deque
input = sys.stdin.readline

n , m = map(int, input().split())
li = list(set(map(int, input().split())))
li.sort()
result = []
def back():
    if len(result)== m:
        print(*result)
        return
    for i in li:
        if (result and result[-1] <= i) or not result:
            result.append(i)
            back()
            result.pop()

back()
