import sys, math
input = sys.stdin.readline

n = int(input())
word = input().strip()
op = ['-', '+','*','/']
def oper(op, a, b):
    if op == '-':
        return b-a
    elif op == '+':
        return a+b
    elif op == '*':
        return a*b
    else:
        return b/a

num = {}
for i in range(n):
    num[chr(ord('A')+i)] = int(input())

stack = []
idx = 0
tmp = 0
for w in word:
    if w not in op:
        stack.append(num[w])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(oper(w,a,b))
print('{:.2f}'.format(stack[0]))

