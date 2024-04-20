import sys
input = sys.stdin.readline
A = int(input())
num = list(map(int,input().split()))
dp = [1] *(A)
for i in range(1,A):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))