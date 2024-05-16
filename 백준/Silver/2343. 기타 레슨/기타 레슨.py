import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

start, end = max(num), sum(num)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 1
    for number in num:
        if total + number > mid:
            cnt += 1
            total = 0
        total += number

    if cnt <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
