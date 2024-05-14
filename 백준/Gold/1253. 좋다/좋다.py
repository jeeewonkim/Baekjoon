import sys

input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))

now = n-1
cnt = 0
while now >=0:
    #print(num[now])
    start , end = 0, n-1
    while True:
        if now == start:
            start +=1
        elif now == end:
            end -=1
        if start >= end:
            now -=1
            break
        if num[now] == num[start]+num[end]:
            cnt +=1
            now -=1
            break
        elif num[now] < num[start]+num[end]:
            end -=1
        else:
            start +=1
    else:
        now -=1

print(cnt)

