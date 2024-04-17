#꿍의 피보나치 수
import sys
input = sys.stdin.readline

n = int(input())


num = list(int(input()) for _ in range(n))

koong = [1,1,2,4]
large = max(num)
for i in range(4,large+1):
    koong.append(koong[i-1]+koong[i-2]+koong[i-3]+koong[i-4])

for i in num:
    print(koong[i])