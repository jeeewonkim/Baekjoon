import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

left, right, sum, res = 0,0, 0, 1e9
while True:
    if sum >= m:
        res = min(res, right- left)
        sum -= num[left]
        left +=1
    elif right == n :
        break
    else:
        sum += num[right]
        right+=1


if res == 1e9:
    print(0)
else:
    print(res)