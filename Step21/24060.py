# def merge_sort(A, p , r):  # A[p..r]을 오름차순 정렬한다.
#     if (p < r) :
#         q = (p + r) // 2;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합


# def merge(A, p, q, r):
#     i = p; j = q; t = r
#     tmp = []
#     while i<= q and j <= r:
#         if A[i] <= A[j]:
#             tmp[t] = A[i]
#             t+=1; i +=1
#         else:
#             tmp[t] = A[j]
#             t+=1; i+=1
#     while i<=q:
#         tmp[t] = A[i]
#         t+=1; i+=1
#     while j <= r:
#         tmp[t] = A[j]
#         t+=1; j +=1
#     i = p; t = 1
#     while(i<=r):
#         A[i] = tmp[t]
#         i+=1; t+=1

# A = [4,5,1,3,2]     
# print(merge_sort(A, 0, 4))



def merge_sort(arr):
    def sort(low, high):
        if high-low< 2:
            return
        mid = (low+high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        
    def merge(low, mid, high):
        temp = []
        l, m = low, mid
        
        while l < mid and m < high:
            if arr[l] < arr[m]:
                temp.append(arr[l])
                l+=1
            else:
                temp.append(arr[m])
                m+=1
            
        while l < mid:
            temp.append(arr[l])
            l+=1
        while m< high:
            temp.append(arr[m])
            m+=1
            
        for i in range(low, high):
            arr[i] = temp[i-low]
            
        return sort(0,len(arr))
    
arr = [4,5,1,3,2]
print()