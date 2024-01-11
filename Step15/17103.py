import sys

tc = int(sys.stdin.readline())
m = 1000000

arr = [True for _ in range(m+1)]
prime = []
arr[0], arr[1] = False, False
for i in range(2, int(m**0.5)+1):
    if arr[i] == True:
        # prime.append(i)
        j = 2
        while i*j <= m:
            arr[i*j] = False
            j+=1

for i in range(tc):
    count =0
    n = int(sys.stdin.readline())
    
    for j in range(2, n//2+1):
        if arr[j] and arr[n-j]:
            count +=1
        
    print(count)
    # for p in prime:
    #     if p > n//2:
    #         break
    #     if n-p in prime:
    #         count +=1
    #print(count)
    # arr1 = arr[0:n+1]
    # count = 0
    # mid = n //2
    # if arr1[mid] == True:
    #     count +=1
    # for i in range(1, mid+1):
    #     if arr1[mid+i]== True and arr1[mid-i] ==True:
    #         count +=1
