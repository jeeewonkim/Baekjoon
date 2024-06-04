import sys
input = sys.stdin.readline
n = int(input())
stick = []
for _ in range(n):
    stick.append(int(input()))

cnt = 1
h = stick[-1]
while stick:
    now = stick.pop()
    if now > h:
        h = now
        cnt +=1
print(cnt)