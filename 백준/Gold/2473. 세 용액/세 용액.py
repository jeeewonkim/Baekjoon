import sys

input = sys.stdin.readline

n = int(input())
liq = sorted(list(map(int, input().split())))

start, end = 0, n-1
total_min =4000000001
answer = []
#print(liq)
def find():
    global start, end, answer, total_min
    while 1<end:
        mid = end -1
        cri = liq[end]
        start = 0
        while start<mid:
            left = liq[start]
            right = liq[mid]
            total = left+right+cri
            #print(start, mid, end, total)
            if total == 0:
                return [left,right,cri]

            if abs(total) < total_min:
                total_min =abs(total)
                answer = [left,right,cri]

            if total < 0:
                start +=1
            elif total > 0:
                mid -=1
        end -=1

    return answer

print(*find())



