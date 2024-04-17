import sys

input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

num.sort()
result = []
def back():
    if len(result) == m:
        print(" ".join(map(str,result)))
        return

    for i in num:
        if (result and result[-1] <=i) or not result:
            result.append(i)
            back()
            result.pop()

back()