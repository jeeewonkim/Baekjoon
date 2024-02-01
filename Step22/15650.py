#N과 M(2)
import sys
n, m = map(int, sys.stdin.readline().split())

# result = []

# def back():
#     if len(result) ==  m :
#         print(" ".join(map(str, result)))
#         return
#     for i in range(1, n+1):
#         if i not in result:
#             if (result and result[-1] < i) or not result:
#                 result.append(i)
#                 back()
#                 result.pop()

            
# back()

#visited 방식
visited = [False for _ in range(n)]

def back(result):
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        if not visited[i] and (not result or result[-1] > i+1):
            result.append(i+1)
            visited[i] = True
            back(result)
            visited[i]= False
            result.pop()

back([])