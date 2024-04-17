#파도반 수열

import sys

input=sys.stdin.readline


T = int(input())

n = [int(input()) for _ in range(T)]
tri = [0] * (max(n)+2)

tri[1],tri[2],tri[3] = 1,1,1


for i in range(4, len(tri)):
    tri[i] = tri[i-3] + tri[i-2]

for i in n:
    print(tri[i])