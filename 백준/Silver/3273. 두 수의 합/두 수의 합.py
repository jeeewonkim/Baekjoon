import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
x = int(input())
#print(num)
front, back = 0, n-1
res = 0
while front < back:
    if num[front] + num[back] == x:
        res +=1
        front +=1
        back -=1
    elif num[front] +num[back] > x:
        back-=1
    else:
        front +=1

print(res)
