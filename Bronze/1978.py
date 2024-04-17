#소수 찾기
n = int(input())
m = list(input().split())
cnt = 0;
for i in m:
    isPrime = False if int(i) == 1 else True
    for j in range(2,int(i)):
        if int(i)%j ==0:
            isPrime = False
            break

print(cnt)