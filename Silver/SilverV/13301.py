#타일 장식물
import sys
input = sys.stdin.readline
n = int(input())
dp = [0,4,6]
for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n])