#N과 M(4)
import sys
n, m = map(int, sys.stdin.readline().split())
rst = []
def back():
    if len(rst) == m:
        print(" ".join(map(str, rst)))
        return
    for i in range(1, n+1):
        if (rst and rst[-1]<=i) or not rst:
            rst.append(i)
            back()
            rst.pop()

back()