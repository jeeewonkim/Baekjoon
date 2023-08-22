# max_len =0
# words=[]
# result = []
# for i in range(5):
#     s = list(input())
#     words.append(s)
#     if len(s) > max_len:
#         max_len = len(s)

# for i in range(5):
#     for dif in range(max_len-len(words[i])):
#         words[i].append("")

# for col in range(0,max_len):
#     for row in range(0,5):
#         result.append(words[row][col])

# r = (' '.join(s for s in result)).replace(" ","")
# print(r)

words = [list(input()) for _ in range(5)]
s = ''
for length in range(15):
    for row in range(5):
        if length < len(words[row]) :
            s+= words[row][length]

print(s)