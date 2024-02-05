from itertools import combinations
def findPrime(n):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for d in range(2, int(n**0.5)+1):
        if n%d == 0:
            return False
    else:
        return True

def solution(nums):
    answer = 0
  
    c = list(combinations(nums, 3))
    for i in c :
        if findPrime(sum(i)):
            answer+=1
    return answer


        
nums = [1,2,7,6,4]
nums.sort()
print(solution(nums))