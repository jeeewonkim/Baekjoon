import sys
sentence = "a"
while True:
    li = []
    sentence = input()
    if sentence == '.':
        break
    else :
        for s in range(len(sentence)):
            if sentence[s] == '(':
                li.append('(')
            elif sentence[s] == '[':
                li.append('[')
            
            elif sentence[s] == ')':
                if not li or li.pop() != '(':
                    print("no")
                    break

                    
            elif sentence[s] == ']':
                if not li or li.pop()!='[':
                    print("no")
                    break

        else:
            if not li :
                print("yes")
            else:
                print("no")
        

# [ , ( 