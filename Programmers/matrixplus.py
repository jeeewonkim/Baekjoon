def solution(arr1, arr2):
    # answer = []
    # for i in range(len(arr1)):
    #     plus = []
    #     for j in range(len(arr1[i])):
    #         plus.append(arr1[i][j] + arr2[i][j])
            
    #     answer.append(plus)
            
    return  [[a+b for a, b in zip(a,b)]for a, b in zip(arr1, arr2)]


arr1 = [[1],[2]]
arr2 = [[3],[4]]

print(solution(arr1, arr2))