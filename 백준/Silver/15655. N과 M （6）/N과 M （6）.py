import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
res = []
def back():
    if len(res) == m:
        print((" ".join(map(str,res))))
        return
    for i in range(n):
        if (res and num[i] > res[-1]) or not res:
            res.append(num[i])
            back()
            res.pop()
back()