import sys
n, k = map(int, sys.stdin.readline().split())

coin = []
count = 0
for i in range(n):
    m = int(sys.stdin.readline())
    if m <= k :
        coin.append(m)
coin.sort(reverse=True)

for c in coin:
    if c <= k:
        count += k // c
        k  %= (k//c)*c
        if k <= 0:
            break
print(count)