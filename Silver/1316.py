n = int(input())
count = 0
for loop in range(n):
    is_group = True
    word = list(input())
    for alp in set(word):
        count_list = []
        if word.count(alp) > 1:
            for w in range(0,len(word)):
                if word[w] == alp:
                    count_list.append(w)
            for d in range(0,len(count_list)-1):
                if count_list[d+1] - count_list[d] != 1:
                    is_group= False
                    break
                else:
                    is_group = True
            if is_group==False:
                break
    if is_group == True :
        count+=1
print(count)

# n = int(input())
# for i in range(n):
#     s = list(input())
#     for j in range(len(s)):
#         if s[j]
        
    