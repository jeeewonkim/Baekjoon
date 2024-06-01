import sys
input = sys.stdin.readline

s1 , s2 = map(str, input().split())

ls1, ls2 = len(s1), len(s2)
result = []
for i in range(ls2-ls1+1):
    cnt = 0
    for j in range(ls1):
        if s1[j] != s2[i+j]:
            cnt +=1
    result.append(cnt)

print(min(result))