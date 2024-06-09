import sys
input = sys.stdin.readline
n = int(input())

a = [False,False] + [True] *(n-1)
primes =[]
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

end, cnt, s = 0,0,0
for start in range(len(primes)):
    while s < n and end < len(primes):
        s += primes[end]
        end +=1
    if s == n:
        cnt +=1
    s -= primes[start]

print(cnt)