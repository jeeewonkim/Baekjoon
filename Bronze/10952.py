result =[]
while 1:
    a,b = map(int, input().split())
    if a ==0 and b ==0:
        break
    result.append(a+b)
for a in result:
    print(a)
    