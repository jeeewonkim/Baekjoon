import sys
n = int(sys.stdin.readline())
result =[]
for i in range(1,n+1):
    a,b = map(int, sys.stdin.readline().split())
    result.append(a+b)
for i in result:
    print(i)