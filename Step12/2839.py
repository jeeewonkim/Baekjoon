import sys

n = int(sys.stdin.readline())
count = 0
while n > 0:
   
    if n % 5 == 0:
        count += n//5
        n -= 5*(n//5)
    
    else:
        count += 1
        n -=3
    
    if n == 0 :
        print(count)
        break
    
    elif n < 0 :
        print(-1)
