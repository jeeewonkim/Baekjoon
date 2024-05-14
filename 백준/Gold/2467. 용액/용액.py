import sys

input = sys.stdin.readline

n = int(input())
liq = sorted(list(map(int, input().split())))

left, right = 0 ,n-1
dif = 2000000000
answer = [liq[left], liq[right]]
while left<right:
    left_liq = liq[left]
    right_liq = liq[right]
    s = left_liq+right_liq
    if s == 0:
        answer = [left_liq, right_liq]
        break
    elif abs(s)<dif:
        dif = abs(s)
        answer = [left_liq, right_liq]
    if s<0:
        left +=1
    else:
        right -=1

print(*answer)