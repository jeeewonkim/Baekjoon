n = int(input())
array =[]
result =[]
for i in range(n):
    p = input().split()
    array.append(p)
for a in range(n):
    for b in range(n):
        l =[]
        if a==b:
            continue
        if int(array[b][0]) in range(int(array[a][0]), int(array[a][0])+10):
            l.append(abs(int(array[a][0])+10-int(array[b][0])))
            result.append(l)
print(result)
