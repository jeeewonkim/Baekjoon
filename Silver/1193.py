n = int(input())
r = 0; k=0
while r<n:
    k+=1
    r = r+k
if(k%2 == 0):
    i = k-(r-n); j = 1+r-n
else:
    i = 1+r-n; j = k-(r-n)
print("{}/{}".format(i,j))