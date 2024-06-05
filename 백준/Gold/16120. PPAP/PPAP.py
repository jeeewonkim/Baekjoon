import sys
input = sys.stdin.readline

word = list(input().strip())
stack = []
idx=0
for w in word:
    stack.append(w)
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
    print("PPAP")
else:
    print("NP")


