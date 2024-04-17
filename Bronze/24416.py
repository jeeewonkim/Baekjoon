#피보나치 수 (1)
import sys

n = int(sys.stdin.readline().strip())
d = [0] * (n + 1)
d[1], d[2] = 1, 1
count, count2 = 0, 0


# 재귀
def fibo1(n):
    a,b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b
    # global count
    # if n == 1 or n == 2:
    #     count += 1
    #     return 1
    # else:
    #     return (fibo1(n - 1) + fibo1(n - 2))


# DP
def fibo2(n):
    return n - 2
    # global count2
    # for i in range(3, n + 1):
    #     d[n] = d[i - 1] + d[i - 2]
    #     count2 += 1
    # return d[n]


print(fibo1(n), fibo2(n))
