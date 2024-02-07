#공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())

house = list(int(sys.stdin.readline()) for _ in range(n))

house.sort()

start, end = 1, house[-1]- house[0]

while start<= end:
    mid = (start+end)//2
    position = house[0]
    count = 1
    
    for i in range(1, n):
        if house[i] >= position+mid :
            count +=1
            position = house[i]
            
    if count >= c:
        start = mid + 1
        
    else:
        end = mid -1

print(end)
    
    

