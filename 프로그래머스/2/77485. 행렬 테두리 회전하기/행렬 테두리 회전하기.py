import copy
def solution(rows, columns, queries):
    answer = []
    graph = [[i+j for i in range(columns)] for j in range(1,rows*(columns),columns)]
    #print(graph)



    after = [i.copy() for i in graph]

    for q in queries:
        mini = rows * columns
        before = [i.copy() for i in after]
        #윗면
        for i in range(q[1], q[3]):
            after[q[0]-1][i] = before[q[0]-1][i-1]
            mini = min(mini, after[q[0]-1][i])

        #아래
        for i in range(q[3]-2,q[1]-2,-1):
            after[q[2]-1][i] = before[q[2]-1][i+1]
            mini = min(mini, after[q[2]-1][i])

        #왼쪽
        for i in range(q[2]-2, q[0]-2, -1):
            after[i][q[1]-1] = before[i+1][q[1]-1]
            mini = min(mini,after[i][q[1]-1])


        # 오른쪽
        for i in range(q[0], q[2]):
            after[i][q[3] - 1] = before[i - 1][q[3] - 1]
            mini = min(mini, after[i][q[3] - 1])

        answer.append(mini)



    return answer
