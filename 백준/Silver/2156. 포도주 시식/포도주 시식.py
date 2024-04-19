import sys
input = sys.stdin.readline

n = int(input())


g = list(int(input()) for _ in range(n))
dp = [0 for _ in range(n)]


if n >2:
    dp[0] = g[0]
    dp[1] = g[0] + g[1]
    dp[2] = max(g[0] + g[1], g[1] + g[2], g[0]+g[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+g[i-1]+g[i], dp[i-2]+g[i], dp[i-1])
    print(max(dp))
else:
    print(sum(g))
