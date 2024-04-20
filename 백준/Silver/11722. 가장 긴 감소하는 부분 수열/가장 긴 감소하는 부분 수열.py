import sys
input = sys.stdin.readline

A = int(input())
n = list(map(int, input().split()))
dp = [1] *(A)

for i in range(1,A):
    for j in range(i):
        if n[i] < n[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))