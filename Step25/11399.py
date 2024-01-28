import sys

n = int(sys.stdin.readline().strip())

atm = list(map(int, sys.stdin.readline().split()))

atm.sort()
r = 0
rr= []
for i in atm:
    r += i
    rr.append(r)
    
print(sum(rr))