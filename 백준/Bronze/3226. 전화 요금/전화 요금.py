import sys

input = sys.stdin.readline

N = int(input())
fee = 0
for i in range(N):
    time, d = map(str, input().split())
    hour, min = map(int, time.split(':'))
    d = int(d)
    if min + d > 60:
        if hour == 6:
            fee+= ((min+d)%60)*10
            fee += ((60-min))*5
            continue
        if hour == 18:
            fee += ((min + d) % 60) * 5
            fee += ((60 - min)) * 10
            continue

    if 7 <= hour < 19:
        fee += d * 10
    else:
        fee += d * 5
print(fee)
