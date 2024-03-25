import sys
input = sys.stdin.readline
T = int(input())


zero = [0] *(41)
one = [0] *(41)
zero[0], zero[1] = 1,0
one[0], one[1] = 0 , 1

for i in range(T):
    N = int(input())
    for i in range(2,N+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    print(zero[N] , one[N])