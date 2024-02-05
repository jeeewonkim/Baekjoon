def solution(n,a,b):
    answer = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print(((((a-1)//2)+1)-1)//2+1)
    # print(((b-1)//2)+1)
    while True:
        a = (a-1)//2 +1
        b = (b-1)//2+1
        if a == b:
            answer+=1
            return answer
        answer+=1

print(solution(8,5,7))