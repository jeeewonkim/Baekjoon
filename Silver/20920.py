import sys

n, m = map(int, sys.stdin.readline().split())
words = []
for i in range(n):
    s = sys.stdin.readline().strip()
    
    if len(s)>=m:
        words.append(s)
        
words_dict = {w : 0 for w in words}

for w in words:
    words_dict[w] +=1
    
sorted_words_dic = dict(sorted(words_dict.items(), key = lambda item: (-item[1], -len(item[0]), item[0])))



for p in sorted_words_dic.keys():
    print(p)