#소수
m = int(input())
n = int(input())
s = []; p = 0
for i in range(m,n+1):
    isPrime = False if int(i) == 1 else True
    for j in range(2,i):
        if i%j == 0:
            isPrime = False
            break        
    if isPrime == True:
        s.append(i)
print("{}\n{}".format(sum(s),s[0]) if len(s)!=0 else -1)