import sys

num = sys.stdin.readline().strip().split('-')
for i in range(len(num)):
    if '+' in num[i]:
        s = num[i].split('+')
        result = 0
        for j in s:
            result +=int(j)
        num[i] = result
result = int(num[0])
for i in range(1, len(num)):
    result -= int(num[i])
    
print(result)
# sub = []
# plus = []
# for n in range(len(num)):
#     if num[n] == '-':
#         sub.append(n)
#     if num[n] == '+':
#         plus.append(n)
        
# print(sub, plus)