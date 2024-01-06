n = int(input())
stack=[]
for i in range(n):
    m = int(input())
    if m == 0 :
        stack.pop()
    else:
        stack.append(m)
    
print(sum(stack))