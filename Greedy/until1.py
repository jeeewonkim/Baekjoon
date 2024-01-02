#1이 될 때까지
n,k = map(int,(input().split()))
count=0
while n>1:
    print(n)
    if n%k == 0:
        count+= 1
        n = int(n/ k)
    else:
        count += int(n%k)
        n -= int(n%k)
print(count-1)