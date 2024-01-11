import sys
from math import gcd

n = int(sys.stdin.readline())

tree = [int(sys.stdin.readline().strip()) for _ in range(n)]

dif = []

for i in range(1,n):
    dif.append((tree[i])-(tree[i-1]))
    
dif_list = sorted(list(set(dif)))
#최대공약수 구하는
# r =1 
# for i in range(len(dif_list)-1):
#     a = dif_list[i+1]
#     b= dif_list[i]
#     while b > 0 :
#         a, b = b, a % b
#     r = a
g = dif[0]
for i in range(1, len(dif)):
    g = gcd(g, dif[i])

count = 0

for i in dif:
    count += (i//g)-1
    
print(count)