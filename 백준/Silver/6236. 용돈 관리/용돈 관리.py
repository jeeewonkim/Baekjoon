import sys

input = sys.stdin.readline

n, m = map(int, input().split())
money = [0] * (n)
money_sum = 0
for i in range(n):
    a = int(input())
    money_sum  += a
    money[i] = a

start, end = max(money), money_sum
answer = 0
while start<=end:
    mid = (start+end)//2
    day = 1
    total = 0
    for mon in money:
        if total+mon > mid:
            day +=1
            total = 0
        total+=mon
    if day <= m:
        end = mid -1
        answer = mid
    else:
        start = mid+1
print(answer)