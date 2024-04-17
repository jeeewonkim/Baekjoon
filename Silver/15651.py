#N과 M(3)
import sys
n, m = map(int, sys.stdin.readline().split())
rst = []
def back():
    if len(rst) == m:
        print(" ".join(map(str, rst)))
        return
    for i in range(1, n+1):
        rst.append(i)
        back()
        rst.pop()

back()