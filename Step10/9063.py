#대지
n = int(input())
x = []; y = []
for i in range(n):
    x_p, y_p = map(int, input().split())
    x.append(x_p); y.append(y_p)
print((max(x)-min(x))*(max(y)-min(y)))