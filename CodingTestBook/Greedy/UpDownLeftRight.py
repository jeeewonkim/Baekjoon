n = int(input())
direction = input().split()
order = ['L','R','U','D']
x = [0,0,-1,1]
y = [-1,1,0,0]
x_p,y_p = 1,1
#첫번째 방법
# for d in direction:
#     if d == "R":
#         if y + 1 in range(1,n+1):
#             y += 1
#     if d == "L":
#         if y - 1 in range(1,n+1):
#             y -=1
#     if d == "D":
#         if x +1 in range(1, n+1):
#             x +=1
#     if d == "U":
#         if x -1 in range(1,n+1):
#             x-=1
# print(x, y)

#두번째 방법
for i in direction:
    for j in range(len(order)):
        if order[j] == i:
            x_r = x_p+ x[j]
            y_r = y_p+ y[j]
    
    if x_r > n or x_r < 1 or y_r > n or y_r < 1:
        continue
    x_p, y_p = x_r, y_r
print(x_r, y_r)
            

    