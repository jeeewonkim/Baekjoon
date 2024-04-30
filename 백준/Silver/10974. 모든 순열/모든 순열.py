import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
num = [ i for i in range(1, n+1)]
perm = list(permutations(num, n))
for p in perm:
    print(*p)
