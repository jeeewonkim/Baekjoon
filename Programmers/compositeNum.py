def solution(n):
    answer = 0
    for i in range(4,n+1):
        for d in range(2,i):
            if i % d == 0:
                answer+=1
                break
    return answer

print(solution(15))