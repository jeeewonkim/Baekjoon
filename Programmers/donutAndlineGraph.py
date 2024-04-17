edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
         [11, 9], [3, 8]]


def solution(edges):
    graph = [[] for _ in range((max(max(edges)) + 1))]

    count = [0] * (len(graph) + 1)
    result = [0] * (4)
    for e in edges:
        graph[e[0]].append(e[1])
        count[e[1]] += 1


    for i in range(len(graph)):

        # 8자 모양 그래프
        if len(graph[i]) == 2 and count[i] >= 1:
            result[3] += 1
        # 생성한 정점
        if len(graph[i]) >= 2 and count[i] == 0:
            result[0] = i

        # 막대그래프
        if len(graph[i]) == 0 and count[i] >= 1:
            result[2] += 1

        result[1] = len(graph[result[0]]) - result[2] - result[3]

    return result

print(solution(edges))
