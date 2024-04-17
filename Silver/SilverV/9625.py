#BABBA

import sys
input = sys.stdin.readline

k = int(input())

dp = [[0,0],[0,1],[1,1]]

for i in range(3,k+1):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])

print(*dp[k])