import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
array = []
visited = [False] * (n)

def find():
    if len(array) == m:
        print(*array)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != num[i]:
            visited[i] = True
            array.append(num[i])
            remember = num[i]
            find()
            visited[i] = False
            array.pop()

find()