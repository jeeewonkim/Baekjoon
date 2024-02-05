# #최고의 집합

#최고의 집합
def solution(n,s):
    if s < n :
        return [-1]
    answer = [s//n for _ in range(n)]

    if s%n == 0:
        return sorted(answer)
    for i in range(s%n):
        answer[i] +=1
    return sorted(answer)

print(solution(3,10))
# r=[]
# max_r = 1
# answer = []

# def perm(n,s):
#     global answer, r
#     result = 1
#     max_r = 1
#     if n>s:
#         answer =[-1]
#         return
#     if len(r) == n:
#         if sum(r) == s:
#             for i in r:
#                 result *= i
#         if max_r < result:
#             answer = [a for a in r]
#         return
#     for i in range(1, s-(n-1)+1):
#         if (r and r[-1]<=i) or not r:
#             r.append(i)
#             solution(n,s)
#             r.pop()

# def solution(n, s):
#     perm(n,s)
#     return answer
                
# print(solution(5,8))
# from itertools import combinations


# def solution(n,s):
#     num = [i for i in range(1, s)]
#     com =list(combinations(num,3))
#     for c in com:
#         if sum(c)== s:
#             for i in range c:
#                 r