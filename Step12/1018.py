import sys

n, m = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().strip() for _ in range (n)]
result = []
for start_y in range(n-7):
    for start_x in range(m-7):
        w_draw = 0
        b_draw = 0
        
        for y in range(start_y, start_y+8):
            for x in range(start_x, start_x+8):
                if (x+y)%2 == 0:
                    if chess[y][x] != 'W':
                        b_draw+=1
                    if chess[y][x] != 'B':
                        w_draw+=1
                else:
                    if chess[y][x] != 'B':
                        b_draw+=1
                    if chess[y][x] != 'W':
                        w_draw+=1
        result.append(b_draw)
        result.append(w_draw)
                
print(min(result))

#3일간 시도했으나 시작이 white/ 시작이 black 일 두가지 경우를 고려하지 못함
# import sys, copy
# n, m = map(int, sys.stdin.readline().split())
# chess_original = [list(sys.stdin.readline().strip()) for _ in range (n)]
# chess = copy.deepcopy(chess_original)
# start_y = 0 
# start_x = 0
# result = []
# count = 0
# cnt = 0
# # while start_x+8<=m:
# while start_y+8<=n:
#     start_x = 0
#     while start_x+8<=m:
#         chess = copy.deepcopy(chess_original)
#         for y in range(start_y, start_y+7):
#             #print(y, start_x, chess[y][start_x], chess[y+1][start_x])
#             if chess[y][start_x] == chess[y+1][start_x]:
#                 count +=1
#                 if chess[y][start_x] == 'W':
#                     chess[y+1][start_x] = 'B'
#                 elif chess[y][start_x] == 'B':
#                     chess[y+1][start_x] = 'W'
#                 #print("1~~", start_y, start_x, count)
#         for y in range(start_y, start_y+8):    
#             for x in range(start_x, start_x + 7):
#                 if chess[y][x] == chess[y][x+1]:
#                     print(y,x+1)
#                     count+=1
#                     if chess[y][x] == 'W':
#                         chess[y][x+1] = 'B'
#                     elif chess[y][x] == 'B':
#                         chess[y][x+1] = 'W'
#         #print(start_y, start_x, count)
#         start_x+=1   
#         result.append(count)
#         count = 0
#     start_y+=1
# print(result)
    