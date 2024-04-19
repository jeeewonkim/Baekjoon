import sys
input = sys.stdin.readline


dp = [[1,0,0],[0,1,0],[1,1,1]] + [[0,0,0] for _ in range(3,100001)]
for i in range(3,100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2])%1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%1000000009
n = int(input())
for i in range(n):
    num = int(input())
    print(sum(dp[num-1])%1000000009)