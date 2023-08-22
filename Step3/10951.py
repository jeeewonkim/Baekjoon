result =[]
while 1:
    try:
        a,b = map(int, input().split())
        result.append(a+b)
    except:
        break
for a in result:
    print(a)