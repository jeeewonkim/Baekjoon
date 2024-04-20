import sys
input = sys.stdin.readline

n = int(input())
dp = list(i for i in range(1, 11))
# + [[0]*9 for _ in range(n-1)]

for i in range(1,n):
    for j in range(1,10):
        dp[j] += dp[j-1]

print(dp[-1]%10007)