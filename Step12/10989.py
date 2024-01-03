#카운팅 정렬(계수 정렬)을 사용한
#시간 복잡도 O(N) , 최악 O(N+K)
n = int(input())
num = [int(input()) for _ in range(n)]
count = [0] * (max(num)+1)

for n in num:
    count[n] +=1
    
print(num)
print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i)

