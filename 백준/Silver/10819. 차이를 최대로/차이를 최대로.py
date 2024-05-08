import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
perm = list(permutations(num,n))

max_sum = 0
for i in range(len(perm)):
    #print(perm[i])
    sum = 0
    for j in range(1,n):
        sum += abs(perm[i][j] - perm[i][j-1])
    max_sum = max(max_sum, sum)
print(max_sum)