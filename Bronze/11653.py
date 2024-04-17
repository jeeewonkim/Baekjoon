#소인수분해
n = int(input())
for i in range(2,n+1):
    if n%i == 0:
        while n%i == 0:
            print(i)
            n/=i
            
# s = []; k = 0
# for i in range(2,n+1):
#     isPrime = False if int(i) == 1 else True
#     for j in range(2,i):
#         if i%j == 0:
#             isPrime = False
#             break        
#     if isPrime == True:
#         s.append(i)

# while int(n)>1:
#     if n%s[k] == 0:
#         print(s[k])
#         n/=s[k]
#         print(n)
#     else:
#         k+=1