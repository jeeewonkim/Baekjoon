#좌표 압축 

#예제 입력
# 5
# 2 4 -10 4 -9

#출력
# 2 3 0 3 1

n = int(input())
point = list(map(int, input().split()))
s_point = sorted(list(set(point)))
dic = {s_point[i] : i for i in range(len(s_point))}
for i in point:
    print(dic[i], end = ' ')
# result = [sum(1 for j in set(pont) if point[i]>j) for i in range(n) ]
# print(*result)

#s_point = set(point)

# for i in range(len(point)):
#     for j in s_point:
#         if point[i] > j:
#             result[i]+=1