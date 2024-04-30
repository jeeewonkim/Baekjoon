import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()
res = []
def find():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        res.append(num[i])
        find()
        res.pop()

find()