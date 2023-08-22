aToz = [chr(i) for i in range(65,91)]
tenAToZ = [j for j in range(10, 36)]
n, b = map(int,input().split())
result = []
while(n>0):
    div = n%b
    if div in range(10,36):
        result.insert(0,aToz[tenAToZ.index(div)])
    else:
        result.insert(0,div)
    n= int(n/b)
for i in result:
    print(i,end='')