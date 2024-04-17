import sys

n = int(sys.stdin.readline().strip())
name = ['ChongChong']
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if a in name and b not in name:
        name.append(b)
    if b in name and a not in name:
        name.append(a)

print(len(name))