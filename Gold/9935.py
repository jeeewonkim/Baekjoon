import sys
input = sys.stdin.readline
s = list(input().strip())
b = list(input().strip())
b_len = len(b)
res = []
for i in range(len(s)):
    res.append(s[i])
    if res[-b_len:] == b:
        for _ in range(b_len):
            res.pop()

if res:
    print(''.join(res))
else:
    print("FRULA")