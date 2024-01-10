import sys

s = sys.stdin.readline().strip()
len_set = set()
for i in range(1, len(s)+1):
    for j in range(0, len(s)):
            len_set.add(s[j : j+i]) 
print(len(len_set))

