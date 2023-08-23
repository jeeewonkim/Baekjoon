#배수와 약수
n=1;m=1
while 1:
    n , m = map(int, input().split())
    if n == 0 and m ==0:
        break
    r= n%m
    if r == n:
        print("factor")
    elif r == 0:
        print("multiple")
    else:
        print("neither")