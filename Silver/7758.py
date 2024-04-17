import sys
n = int(sys.stdin.readline())
dic = dict()
for i in range(n):
    name, state = map(str, sys.stdin.readline().split())
    dic[name] = state

sort_dic = sorted(dic.keys(), reverse=True)

for i in sort_dic:
    if dic[i] == "enter":
        print(i)