import sys
input = sys.stdin.readline

n, p = map(int, input().split())
st = [[] for _ in range(n+1)]
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    while st[a] and st[a][-1] > b:
        cnt += 1
        st[a].pop()
    if st[a] and st[a][-1] == b:
        continue
    st[a].append(b)
    cnt +=1

print(cnt)