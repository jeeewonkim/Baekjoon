n , m = map(int, input().split())
#set
#n_list = set([input() for _ in range(n)])
#n_list.sort()

count =0
#dic
n_list = {input() :True for _ in range(n)}
for i in range(m):
    if input() in n_list.keys():
        count +=1

#set
# for i in range(m):
#     if input() in n_list:
#         count +=1
        
        
#이진 탐색        
# for s in m_list:
#     start =0
#     end = len(n_list)-1
    
#     while start<=end:
#         mid = (start+end)//2
        
#         if s == n_list[mid]:
#             count +=1
#             break
#         elif s > n_list[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
            
print(count)