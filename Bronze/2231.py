import sys

N = int(sys.stdin.readline())
n_int = 0
while  n_int < N :
    n_int +=1
    result = n_int+ sum(map(int, str(n_int)))
    if result == N:
        break
    
print(n_int if n_int !=N else 0)
    