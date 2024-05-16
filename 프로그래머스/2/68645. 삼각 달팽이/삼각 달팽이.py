import sys
sys.setrecursionlimit(10**9)
def solution(n):
    answer = [[0]* i for i in range(1,n+1)]

    num = 1
    top = 0
    for i in range(1, n+1):
        top+= i
    print(top)
    def fill(op, start, end, num,turn):
        if num > top:
            return
        if op == 0:
            for i in range(start, end):
                answer[i][turn] = num
                num +=1

            fill(1, start+1, end ,num,turn)
        elif op ==1 :
            for i in range(turn+1, end-turn):
                answer[end-1][i] = num
                num +=1
            fill(2, end-2, start, num,turn+1)
        elif op == 2:
            for i in range(start, end-1, -1):
                answer[i][-turn] = num
                num +=1
            fill(0, end +1, start+1, num,turn)


    fill(0,0,n,num,0)
    result = []
    for a in answer:
        for ans in a:
            result.append(ans)
    return result

