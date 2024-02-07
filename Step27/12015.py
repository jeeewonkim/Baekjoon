#가장 긴 증가하는 부분 수열 2


import sys

N = int(sys.stdin.readline().strip())
A = set(map(int, sys.stdin.readline().split()))

start = 0
end = len(A)

