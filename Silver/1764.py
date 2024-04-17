import sys

n,m = map(int, sys.stdin.readline().split())

not_hear = {sys.stdin.readline().strip(): True for _ in range(n)}
count = 0
name = []
for i in range(m):
    not_see = sys.stdin.readline().strip()
    if  not_see in not_hear.keys():
        name.append(not_see)
        
name.sort()
print(len(name))
for i in name:
    print(i)