import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
cnt = 0
left, right = 0 , 1
while left <= right and right <= n:
    total = sum(number[left:right])
    if total == m:
        cnt +=1
        right +=1

    elif total < m:
        right +=1
    else:
        left +=1


print(cnt)