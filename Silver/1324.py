import sys

a,b = map(int, sys.stdin.readline().split())

if a < b :
    a1,b1 = b,a
else:
    a1 , b1 = a, b

while b > 0:
    a, b = b, a % b
    
print(a1//a * b1)