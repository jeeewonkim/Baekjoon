#약수들의 합
while 1:
    y=[]
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n%i ==0:
            y.append(i)
    if sum(y) == n:
        print(n, " = ", " + ".join(str(i) for i in y), sep="")
    else:
        print(n, "is NOT perfect")