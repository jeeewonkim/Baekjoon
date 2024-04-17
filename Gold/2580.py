#스도쿠

import sys

input = sys.stdin.readline


#3*3
def square(y, x, n):
    for i in range(3):
            for j in range(3):
                if n == sdk[y//3 * 3 + i][x//3 * 3 + j]: # 칸내에 이미 있으면
                    return False
    return True
#가로
def row(y , n):
    for a in range(9):
        if n == sdk[y][a]:
            return False
    return True
#세로
def column(x, n):
    for a in range(9):
        if n == sdk[a][x]:
            return False
    return True


def find(n):
    if n == len(blank):
        for s in sdk:
            print(*s)
        exit()
        
    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x, i) and row(y, i) and square(y,x,i):
            sdk[y][x] = i
            find(n+1)
            sdk[y][x] = 0
            
blank = []
sdk = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            blank.append([i,j])
            
find(0)



# for i in range(9):
#     for j in range(9):

#         if sdk[i][j] == 0:
#             for n in range(1, 10):
#                 if n not in sdk[((i//3)*3):((i//3)*3+3)][((j//3)*3):((j//3)*3+3)] and n not in sdk[i]:
#                     y_list = []
#                     for y in range(9):
#                         y_list.append(sdk[y][j])
#                     if n not in y_list:
#                         sdk[i][j] = n
                    

# for s in sdk:
#     print(*s)