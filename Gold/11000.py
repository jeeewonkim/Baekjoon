import sys, heapq
input = sys.stdin.readline
N = int(input())

lecture = [list(map(int, input().split())) for _ in range(N)]
lecture.sort()
room = []
heapq.heappush(room, lecture[0][1])

for i in range(1,N):
    if lecture[i][0] < room[0]:
        heapq.heappush(room, lecture[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][1])


print(len(room))