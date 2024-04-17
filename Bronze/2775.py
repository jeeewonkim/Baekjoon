import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apt = [[] for _ in range(k+1)]
    apt[0] = [i for i in range(1,n+1)]
    for i in range(1,k+1):
        for j in range(1,n+1):
            apt[i].append(sum(apt[i-1][0:j]))
    print(apt[k][n-1])