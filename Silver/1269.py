import sys


a,b = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
a_dic = {i: True for i in a_list}
b_dic = {i : True for i in b_list}
for a in a_list:
    if a in b_dic.keys():
        del(b_dic[a])
        
for b in b_list:
    if b in a_dic.keys():
        del(a_dic[b])

print(len(b_dic)+len(a_dic))