import sys, heapq
input = sys.stdin.readline

n,m = map(int, input().split())
a= list(map(int, input().split()))
q = []
heapq.heapify(a)


b = list(map(int, input().split()))
for j in b:
    heapq.heappush(a, j)

for i in range(n+m):
    print(heapq.heappop(a),end = " ")
