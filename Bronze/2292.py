# #벌집
# n = int(input())
# result = 1
# i = 0        
# while(1):
#     if n in range(result+1, result+6*i+1):
#         print(i+1)
#         break
#     else:
#         result += 6*i
#         i +=1
result = 1
cnt = 1
n = int(input())
while (n>result):
    result = result+6*cnt
    cnt+=1
print(cnt)