def solution(sizes):
    big, small = [], []
    for s in sizes:
        big.append(max(s)) 
        small.append(min(s)) 
    
    return max(big)*max(small)

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


print(solution(sizes))


# def solution(sizes):
#     big, small = 0, 0
#     for s in sizes:
#         big = (max(max(s), big))
#         small = (max(min(s), small) )
    
#     return big*small

# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


# print(solution(sizes))