tri = list(map(int,input().split()))
tri.sort()
if tri[2] == tri[1] == tri[0] :
    print(sum(tri))
    
else :
    if tri[2] < tri[0]+tri[1]:
        print(sum(tri))
    else:
        while tri[2] >= tri[0]+tri[1]:
            tri[2] = tri[2]-1
        print(sum(tri))
