import sys
m, n = map(int, sys.stdin.readline().split())
arr = [True for _ in range(n+1)]
arr[0]=False
arr[1] = False

for i in range(2, int(n**0.5)+1):
    if arr[i] ==True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j +=1
        
for i in range(m,n+1):
    if arr[i]:
        print(i)

    

# def prime_numbers(m, n):
#     arr = [i for i in range(m,n+1)]
#     end = int(n**(1/2))
#     for i in range(2, end+1):
#         if arr[i] % i == 0 :
#             continue
#         for j in range(i*i, n+1, i):
#             arr[j] = 0
#     return [i for i in arr[2:] if arr[i]]
        
    
#prime_list = [True for _ in range(m,n+1)]

#print(prime_numbers(m,n))

# arr = [ i for i in range(m, n+1)]
# if m == 1 or n == 1:
#     arr[0] = 0
# for i in range(2, int(n**(1/2))+1):
#     if arr[i] == 0:
#         j = 2
#         while i * j <= n:
#             arr[i*j] = 0
#             j+=1
            
# for i in range(n+1):
#     if arr[i]!=0:
#         print(arr[i])