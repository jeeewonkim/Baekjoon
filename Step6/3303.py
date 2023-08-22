piece = input().split()
origin = [1,1,2,2,2,8]
result=[]
for i in range(0,6):
    result.append(origin[i]-int(piece[i]))
print(*result)