#나무자르기
import sys

n, m = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(h)
while start<= end:
    mid = (start+end) // 2
    s = 0
    for i in h:
        if i > mid:
            s+=i-mid
    
    if s <  m:
        end = mid -1
    else:
        start = mid + 1
        
print(end)
        