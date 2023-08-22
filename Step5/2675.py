n = int(input())
for i in range(n):
    m, s = map(str,input().split())
    for j in s:
        print(j*int(m), end = "")
    print()
        