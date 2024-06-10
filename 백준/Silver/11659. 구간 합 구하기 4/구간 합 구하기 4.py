import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = [0 for _ in range(n)]
arr[0] = num[0]
for k in range(1,n):
    arr[k] = num[k]+arr[k-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        partSum = arr[j-1]
    else:
        partSum = arr[j-1] - arr[i-2]
    print(partSum)