from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

num.sort()

combi = permutations(num, m)

for i in combi:
    print(*i)
