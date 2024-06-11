import sys
input = sys.stdin.readline

n, m = map(int, input().split())
v = list(map(int, input().split()))
right,end, s  = 0, m, 0
res = []
for left in range(n-m+1):
    while right < end and end <= n:
        s+=v[right]
        right +=1
    end +=1
    res.append(s)
    s -= v[left]

ans = max(res)
cnt = 0
if ans == 0:
    print("SAD")
    exit(0)
else:
    for r in res:
        if r == ans:
            cnt +=1
    print(ans)
    print(cnt)
