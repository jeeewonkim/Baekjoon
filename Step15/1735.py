import sys
a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

u1, d1 = a1*b2 + a2*b1, b1*b2

if u1 < d1:
    u2 , d2 = d1, u1
else:
    u2, d2 = u1, d1
    
while d2 > 0:
    u2, d2 = d2, u2%d2
    

print(u1 // u2, d1//u2)
