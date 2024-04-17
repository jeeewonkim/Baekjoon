import sys
input =sys.stdin.readline

def cantorian(n):
    print(n)
    if n == 1:
        return "-"
    else:
        left = cantorian(n//3)
        mid = " " * (n//3)
        return left+mid+left

while True:
    try:
        N = int(input())
        rst = cantorian(3**N)
        print(rst)
    except:
        break
# import sys

# def cantorian(n, array):
#     copy = []

#     for a in array:
#         start = 0
#         while start+n//3<=n:
#             copy.append(list(a[i] for i in range(start, start+n//3)))
#             start+=n//3
#     print(copy)
#     s = 0
#     for i in range(0,len(copy),3):
        
    
#     if n //3 == 1:
#         return copy
#     else:
#         return cantorian(n//3, copy)

# n = 3**int(sys.stdin.readline().strip())
# array = []
# start=0
# while start+n//3<=n:
#         array.append(list(i for i in range(start, start+n//3)))
#         start+=n//3
# array.remove(array[1])
# print(array)
# #r=cantorian(n//3, array)
# result = []
# for i in cantorian(n//3, array):
#     result.append(*i)
# print(result)
# for i in range(n):
#     print("-" if i in result else " ", end = "")