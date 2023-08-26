x = []; y = []
for i in range(3):
    n, m = map(int,input().split())
    x.append(n); y.append(m)
for i in set(x):
    if x.count(i) == 1:
        print(i, end = " ")
for j in set(y):
    if y.count(j) == 1 :
        print(j)