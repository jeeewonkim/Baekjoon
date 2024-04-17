def solution(n, computers):
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return

        if computers[x][y] == 1:
            computers[x][y] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)

    for x in range(n):
        for y in range(n):
            if computers[x][y] == 1:
                dfs(x, y)
                answer += 1
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])