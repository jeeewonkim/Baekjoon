def solution(n, m):
    answer = [1,m*n]
    big = max(n,m)
    small = min(n,m)
    loop = small if big%small ==0 else big
    for i in range(loop,0, -1):
        if big % i == 0 and small % i == 0:
            answer[0] = i
            if i != 1:
                answer[1] =  big if big%small ==0 else big* small //i
            return answer
        
        
print(solution(14,21))