import sys

n = int(sys.stdin.readline().strip())
count = 0
name_set = set()
for i in range(n):
    name = sys.stdin.readline().strip()
    if name == 'ENTER':
        count += len(name_set)
        name_set = set()
    else :
        name_set.add(name)
count += len(name_set)
print(count)