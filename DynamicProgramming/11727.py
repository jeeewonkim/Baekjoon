import sys
input = sys.stdin.readline
n = int(input())
tile = [0 for _ in range(n+1)]
tile[1] = 1
s = 0
for i in range(2,n+1):
    s += tile[i-1]
    plus = 2 if i %2 ==0 else 1
    tile[i] = (s + plus)%10007
print(tile[n])