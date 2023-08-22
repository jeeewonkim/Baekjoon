x = int(input())
n = int(input())
s = 0
for i in range(1,n+1):
    price, num = map(int, input().split())
    s+=price*num
if x==s :
    print("Yes")
else:
    print("No")