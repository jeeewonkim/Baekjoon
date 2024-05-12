import sys
input = sys.stdin.readline
result = 0
li = [False for _ in range(10001)]
def gen(num):
    res = int(num)
    for i in range(len(num)):
        res += int(num[i])
    if res < 10000:
        li[res] = True

    if res < 10001:
        li[res] = True

for i in range(1,10001):
    gen(str(i))

for i in range(1,10001):
    if li[i] == False:
        print(i)
