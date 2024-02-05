def solution(sides):
    answer = 0
    long = max(sides)
    short = min(sides)
    
    # long이 가장 길 때
    for _ in range(long-short+1, long+1):
        answer+=1

    # 새로운 길이가 가장 길 때
    for s in range(long+1, short+long):
        answer+=1
    return answer

sides = [11, 7]

print(solution(sides))