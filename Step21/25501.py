#재귀의 귀재
import sys
def recursion(s,l,r, count):
    result = []
    count +=1
    if l >= r: 
        result.append(1) 
        result.append(count)
        return result
    elif s[l]!=s[r] :
        result.append(0)
        result.append(count)
        return result
    else:
        return recursion(s,l+1, r-1, count)
    
def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s)-1 , count)    


for i in range(int(sys.stdin.readline().strip())):
    print(*isPalindrome(sys.stdin.readline().strip()))

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))