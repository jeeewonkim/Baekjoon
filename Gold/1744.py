import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
res = 0
for _ in range(N):
    num = int(input())
    if num > 1 :
        plus.append(num)
    elif num <= 0 :
        minus.append(num)
    else:
        res +=1
plus.sort(reverse=True)
minus.sort()
for p in range(0,len(plus),2):
    if p+1 >= len(plus):
        res += plus[p]
    else:
        res += (plus[p] * plus[p+1])

for m in range(0,len(minus),2):
    if m+1 >= len(minus):
        res += minus[m]
    else:
        res += (minus[m] * minus[m+1])

print(res)