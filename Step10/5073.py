while 1:
    tri = list(map(int,input().split()))
    if sum(tri) == 0:
        break    
    if sum(tri)> 2*max(tri):
        for i in range(3):
            cnt = tri.count(tri[i])
            if cnt == 3 :
                p="Equilateral"
                break
            elif cnt == 2 :
                p ="Isosceles"
                break
            elif cnt == 1:
                p = "Scalene"
    else:
        p = "Invalid"
    print(p)