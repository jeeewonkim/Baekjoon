import sys


t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(min(a,b), 0, -1):
        if a % j == 0 and b % j == 0:
            print(a // j * b)
            break