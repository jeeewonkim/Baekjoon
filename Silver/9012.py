import sys

n = int(sys.stdin.readline())

isVps = "YES"
for i in range(n):
    li = []
    vps = sys.stdin.readline()
    for v in range(len(vps)):
        if vps[v] == '(':
            li.append(v)
        elif vps[v] == ')':
            if li :
                li.pop()
                isVps = "YES"
            elif not li:
                isVps = "NO"
                break
    if li : isVps = "NO"
        
    print(isVps)

    