#단어정렬
n = int(input())
words = [input() for _ in range(n)]
words_s = (list(sorted(set(words))))
dic = {i : len(words_s[i]) for i in range(len(words_s))}
s_dic = dict(sorted(dic.items(), key = lambda item:item[1]))


for i in s_dic:
    print(words_s[i])