import sys
input = sys.stdin.readline
n = int(input())
s = 0
cnt = 0
start , end = 0 , 0
for start in range(n):
    while s < n and end <n :
        s += end + 1
        end +=1
    if s == n:
        cnt +=1
    s -= start+1
print(cnt)