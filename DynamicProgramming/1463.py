#다이나믹 프로그래밍 1로 만들기

import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 1000001

for i in range(2,n+1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    if i %2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)

print(d[n])