n = int(input())
for i in range(n):
    c = int(input())
    q = int(c/25)
    d = (c%25)
    n = d%10
    p = n%5 
    print(q,int(d/10),int(n/5),p)