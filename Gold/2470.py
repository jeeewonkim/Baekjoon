import sys

input = sys.stdin.readline
N = int(input())
liq = list(map(int, input().split()))
liq.sort()

right = N - 1
left = 0
min_s = 2e+9+1
answer = [liq[left], liq[right]]
while left < right:

    left_liq = liq[left]
    right_liq = liq[right]
    s = left_liq + right_liq

    if s == 0:
        answer = [left_liq, right_liq]
        break

    if abs(s) < min_s:
        min_s = abs(s)
        answer = [left_liq, right_liq]

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1

print(answer[0], answer[1])
