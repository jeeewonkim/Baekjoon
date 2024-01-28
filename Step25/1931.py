#회의실 배정

import sys


n = int(sys.stdin.readline().strip())

meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
meeting.sort(key = lambda x: (x[1], x[0]))


cnt = 1
end = meeting[0][1]
for i in range(1,n):
    if meeting[i][0]>= end:
        cnt +=1
        end = meeting[i][1]
        
print(cnt)
# while m < len(meeting):
#     if m == len(meeting)-1:
#         if meeting[m][0] >= end:
#             count +=1
#             break
#         else:
#             break
#     if meeting[m][0] >= end :
#         if meeting[m][1]- meeting[m][0] > meeting[m+1][1] - meeting[m+1][0]:
#             m+=1 
#         end = meeting[m][1]
#         count +=1
#         # print(meeting[m][0], meeting[m][1])
#     if meeting[m][0] < end:
#         m+=1
#         continue
    # if meeting[m][0] >= start:

    
    # m+=1

# while m < len(meeting):
#     if meeting[m-1][0] >= end :
#         if meeting[m-1][1]- meeting[m-1][0] > meeting[m][1] - meeting[m][0]:
#             m+=1 
#         end = meeting[m-1][1]
#         print(meeting[m][0], meeting[m][1])
#     if meeting[m-1][0] < end:
#         m+=1
#         continue
    
