import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt = 0
    start = 0
    for i in range(n):
        while True:
            if start == m or a[i] <= b[start]:
                cnt += start
                break
            else:
                start+=1

    print(cnt)

