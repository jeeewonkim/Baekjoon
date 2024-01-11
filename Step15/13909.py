import sys

n = int(sys.stdin.readline())
#arr = [1 for _ in range(n+1)]

count = 0 
for i in range(1, int(n**0.5)+1):
    if i*i <= n:
        count +=1
        
print(count)

# for i in range(1, n+1):
#     j = 2
#     while i*j<=n:
#         if arr[i*j] == 0:
#             arr[i*j] = 1
#         elif arr[i*j] == 1:
#             arr[i*j] = 0
#         j+=1
# for j in range(n):
#     if arr[j] == 1:
#         print()