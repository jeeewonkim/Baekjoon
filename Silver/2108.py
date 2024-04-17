import sys, math

n = int(sys.stdin.readline().strip())
count = []
num = list(int(sys.stdin.readline().strip())for _ in range(n))
num_dic={i:0 for i in num}
for i in num:
    num_dic[i] +=1
num.sort()
result = []
sorted_dic = dict(sorted(num_dic.items()))
max_val = max(num_dic.values())
for i in sorted_dic:
    if sorted_dic[i] == max_val:
        result.append(i)  

print(round(sum(num)/n)) #산술평균
print(num[n//2]) # 중앙값
print(result[1] if len(result)>=2 else result[0])# 최빈값
print(num[-1]-num[0]) #범위