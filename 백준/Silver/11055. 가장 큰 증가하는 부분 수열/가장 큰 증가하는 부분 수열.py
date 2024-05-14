import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = A[:]
for i in range(1,n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], A[i]+dp[j])

print(max(dp))