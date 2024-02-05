def solution(n, s):
    answer = []
    s = []
    for i in range(1,n//2+1):
        s.append([i, n-i])
        
    return answer