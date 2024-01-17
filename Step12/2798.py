import sys

n, m = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

max_sum = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = card[i] + card[j] + card[k]
            if  s == m :
                max_sum = m
                break
            if s < m and max_sum < s:
                max_sum = s

print(max_sum)