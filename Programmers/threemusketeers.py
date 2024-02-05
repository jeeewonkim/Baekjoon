from itertools import combinations
def solution(number):
    answer = 0
    n = combinations(number, 3)
    for i in n:
        if sum(i) == 0 :
            answer+=1
    return answer


number =[-2, 3, 0, 2, -5]

print(solution(number))