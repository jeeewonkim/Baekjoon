import sys, math

input = sys.stdin.readline

x, y = map(int, input().split())
first = 100*y // x
change = first
res = 0
start, end = 0, x
if first >=99:
    print(-1)
else:
    while start<=end:
        mid = (start+end)//2
        change = 100*(y+mid)//(x+mid)
        if change > first:
            end = mid -1
            res = mid
        else:
            start = mid +1

    print(res)