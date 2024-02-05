def solution(string):
    answer = 0
    string= [num for num in string.split()]
    for s in range(len(string)):
        if string[s] == 'Z':
            answer-=int(string[s-1])
        else:
            answer+=int(string[s])
    return answer

string = "10 Z 20 Z 1"	
print(solution(string))
      