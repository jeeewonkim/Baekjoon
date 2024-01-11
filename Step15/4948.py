import sys
m = 123456
arr = [True for _ in range(2*m+1)]
arr[0], arr[1] = False, False

for i in range(2, int((2*m)**0.5)+1 ):
    if arr[i] == True:
        j = 2
        while i*j <= 2*m:
            arr[i*j] = False
            j+=1

while True:
    count =0
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    
    for i in range(n+1, 2*n+1):
        if arr[i]:
            count += 1
    print(count)

# while True:
#     n = int(sys.stdin.readline())
#     if n == 0 :
#         break
#     arr = [1 for _ in range((2*n)+1)]
#     arr[0]  = 0 
#     arr[1] = 0
#     for i in range(2, int((2*n)**0.5)+1):
#         if arr[i] == 1:
#             j = 2
#             while i*j <= 2*n :
#                 arr[i*j] = 0
#                 j+=1
#     print(sum(arr[n+1:]))
    

    
    # for i in range(n, 2*n +1):
    #     if i == 1:
    #         continue
        
        # for j in range(2, int(i**0.5)+1):
        #     if i % j == 0 :
        #         break
        # else:
        #     count +=1