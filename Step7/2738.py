n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(2):
    for row in range(n):
        im = input().split()
        for col in range(m):
            matrix[row][col] += int(im[col])

for j in range(0,len(matrix)):
    print(*matrix[j])