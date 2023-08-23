#약수 구하기
n,k = map(int, input().split())
y = []
for i in range(1, n+1):
    if n%i ==0:
        y.append(i)
print(0 if len(y)<k else y[k-1])
