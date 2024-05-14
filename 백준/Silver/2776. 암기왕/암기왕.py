import sys

input = sys.stdin.readline
def find(first, num):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if num == first[mid]:
            return 1
        elif num < first[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0
T = int(input())
for _ in range(T):
    n = int(input())
    first = list(map(int, input().split()))
    m = int(input())
    second = list(map(int, input().split()))
    first.sort()
    for i in second:
        print(find(first, i))