import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
lcs = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if a[j-1] == b[i-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])