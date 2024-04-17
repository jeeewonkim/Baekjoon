import sys
input = sys.stdin.readline
mo = ['a','e','i','o','u']
L,C = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
ans = []
#cnt = 0
def back(start):
    m_cnt = 0
    j_cnt = 0
    if len(ans) == L:
        for a in ans:
            if a not in mo:
                j_cnt+=1
            if a in mo:
                m_cnt+=1
        if m_cnt >=1 and j_cnt>=2:
            print("".join(ans))

    for i in range(start, C):
        ans.append(words[i])
        back(i+1)
        ans.pop()

back(0)
