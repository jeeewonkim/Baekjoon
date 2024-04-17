#랜선 자르기
import sys
n, k = map(int,sys.stdin.readline().split())

line = list(int(sys.stdin.readline()) for _ in range(n))

start = 1
end = max(line)

while(start<=end):
    mid = (start+end)//2
    num = 0
    
    for l in line:
        num += l // mid
        
    if num < k :
        end = mid - 1
        
    else:
        start = mid+1

print(end)