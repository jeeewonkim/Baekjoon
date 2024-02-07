#수 찾기
import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target, start, end):
    if start> end:
        return 0
    
    mid = (start+end) //2
    
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
    else:
        return binary_search(arr, target, mid+1, end)

        
a.sort()

for i in b:
    print(1 if i in a else 0)
    # print(binary_search(a, i, 0, n-1))