def solution(board):
    answer = 0
    n = len(board)
    
    new_board = [[0 for _ in range (n)] for _ in range(n)]

    
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 < y+i < n and 0<x+j < n:
                            new_board[y+i][x+j] = 1

    for b in new_board:
        answer+= b.count(1)
    return n**2 - answer

board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

print(solution(board))