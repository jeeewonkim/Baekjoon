# 계단 오르기

import sys

input = sys.stdin.readline

stair_num = int(input())
stair = []
for _ in range(stair_num):
    stair.append(int(input()))

dp = [0] * (stair_num)
if stair_num == 1:
    print(stair[0])
    exit(0)
elif stair_num == 2:
    print(sum(stair))
    exit(0)
dp[0] = stair[0]
dp[1] = max(stair[0] + stair[1], stair[1])
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, stair_num):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[stair_num - 1])
