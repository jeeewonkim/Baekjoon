import sys

tc = int(sys.stdin.readline())
def is_prime_number(n):
    if n == 0 or n==1:
        return False
    end = int(n**(1/2))
    for i in range(2, end+1):
        if (n%i ==0) :
            return False
    return True

for i in range(tc):
    n = int(sys.stdin.readline())
    
    while True:
        if is_prime_number(n):
            print(n)
            break
        else :
            n+=1