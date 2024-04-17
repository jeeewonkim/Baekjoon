
n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))
n_list.sort()

for i in m_list:
    start = 0
    end = len(n_list) - 1
    exist = 0
    while start <= end:
        mid = (start+end)//2
        
        if i == n_list[mid]:
            exist = 1
            break
        elif i < n_list[mid]:
            end = mid -1
        else:
            start = mid +1
    print(exist , end = " ")