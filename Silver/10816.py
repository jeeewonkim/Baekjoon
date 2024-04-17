import sys

n = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))
#n_dic ={i : 0 for i in range(min(n_list), max(n_list)+1)}
n_dic = {i : 0 for i in n_list}
for i in n_list:
    n_dic[i] +=1
    
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if i in n_dic.keys():
        print(n_dic[i], end = " ")
    else:
        print(0, end = " ")
# #print(n_dic[10])