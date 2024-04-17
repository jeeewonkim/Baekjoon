import sys
n = int(sys.stdin.readline())
result =[]
alist= []
blist = []
for i in range(1,n+1):
    a, b = map(int, sys.stdin.readline().split())
    alist.append(a)
    blist.append(b)
    result.append(a+b)
   
for i in range(len(result)):
    print("Case #{}:".format(i+1),alist[i],"+",blist[i],"=", result[i])