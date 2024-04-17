#연속부분최대곱

import sys
input = sys.stdin.readline


n = int(input())
num = []
for _ in range(n):
    num.append(float(input()))
for i in range(1,n):
    num[i] = max(num[i-1]*num[i], num[i])

print('%0.3f' % max(num))