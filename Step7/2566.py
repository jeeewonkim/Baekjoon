max_value =0
max_row = 0
max_column =0
for row in range(0,9):
    n = input().split()
    max_n = int(max(n))
    if max_value < max_n:
        max_value = max_n
        max_row = row + 1
        max_column = n.index(str(max_n))+1
print(max_value)
print(max_row, max_column)