#카운팅 정렬(계수 정렬)을 사용한
#시간 복잡도 O(N) , 최악 O(N+K)
import sys
n = int(sys.stdin.readline())
#num = [int(input()) for _ in range(n)]
count = [0] * (10000+1)

for i in range(n):
    count[int(sys.stdin.readline())] +=1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i)

