#주유소

import sys

n = int(sys.stdin.readline().strip())

distance = list(map(int,sys.stdin.readline().split()))

price = list(map(int,sys.stdin.readline().split()))
p = price[0]
r = distance[0]*p

for i in range(1,n-1):
    if p > price[i]:
        p = price[i]
    r+= p*distance[i]
    
print(r)