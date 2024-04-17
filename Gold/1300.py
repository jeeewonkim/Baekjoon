#k번째 수 
import sys

n = int(sys.stdin.readline().strip())

k = int(sys.stdin.readline().strip())
start = 1
end = k
while start<=end:
    cnt = 0
    mid = (start+end)//2
    for i in range(1, n+1):
        cnt += min(n, mid // i)
    if cnt >= k:
        end = mid -1
        answer = mid
    else:
        start = mid+1
        
print(answer)