#두 배열의 원소 교체
# N, K -> N은 배열의 크기 K는 최대 바꿀 수 있는 횟수
n, k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
