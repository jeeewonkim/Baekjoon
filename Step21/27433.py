#팩토리얼 2

import sys

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(int(sys.stdin.readline().strip())))