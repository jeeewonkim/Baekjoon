n = int(input())
p = [list(map(str, input().split())) for _ in range(n)]

p.sort(key = lambda x : (int(x[0])))

for i in p:
    print(f"{i[0]} {i[1]}")