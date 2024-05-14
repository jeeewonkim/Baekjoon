import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [10001 for _ in range(m+1)]
num = []
dp[0] = 0
for i in range(n):
    num.append(int(input()))
for number in num:
    for i in range(number, m+1):
        dp[i] = min(dp[i-number]+1, dp[i])
#print(dp)
print(dp[m] if dp[m]!=10001 else -1)