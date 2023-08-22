s = input().upper()
result=[]
s_set = list(set(s))
for i in s_set:
    result.append(s.count(i))
count =0
for i in result:
    if max(result) == i:
        count +=1
        index = result.index(i)
if count > 1:
    print("?")
else:
    print(s_set[index])