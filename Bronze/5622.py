dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
result = 0
for j in range(len(word)):
    for i in dial:
        if word[j] in i:
            result += dial.index(i) +3

print(result)
    #new_dial=[a for a in range(len(dial)) for b in dial[a] if word[i] is b]
