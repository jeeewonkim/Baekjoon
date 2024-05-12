import sys
input = sys.stdin.readline
n = int(input())
num = [str(i) for i in range(10)]
result = []
answer = []


def back(length):
    if len(result) == length:
        a = ''
        for i in result:
            a += str(i)
        num.append(a)
        return
    for i in range(10):
        if result and result[-1] > i or not result:
            result.append(i)
            back(length)
            result.pop()

for i in range(2,11):
    back(i)

if n >= len(num):
    print(-1)
else:
    print(num[n])
