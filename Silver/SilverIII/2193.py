#이친수
import sys
input = sys.stdin.readline

N = int(input())
dp = [0,1,1]

for i in range(3,91):
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])