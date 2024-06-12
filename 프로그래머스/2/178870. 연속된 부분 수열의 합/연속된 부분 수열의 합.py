def solution(sequence, k):
    n = len(sequence)
    right , s, dif = 0,0, 1e9
    ans = []
    for left in range(n):
        while s< k and right< n:
            s += sequence[right]
            right +=1
        if s == k and right-left < dif:
            ans = [left, right-1]
            dif = right-left
        s -= sequence[left]

    return ans
