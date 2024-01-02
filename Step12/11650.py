# n = int(input())
# points = [tuple(map(int, input().split())) for _ in range(n)]

# for x in sorted(set(p[0] for p in points)):
#     y_list = sorted(y for x_point, y in points if x_point == x)
#     for y in y_list:
#         print(x,y)
# x_list, y_list = zip(*point) #정렬안된
# x_set = set(sorted(x_list)) #정렬된
# for c in x_set:
#     c_list = [index for index, value in enumerate(x_list) if value == c]
#     i_list = []

#     for i in c_list:
#         i_list.append(y_list[i]) 
#     is_list = sorted(i_list) 
#     for i in range(len(is_list)):
#         print(c, is_list[i])


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()
for i in points:
    print(i[0], i[1])
