import sys

n = int(sys.stdin.readline())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

# background = [[0 for _ in range(1, max(paper)[0]+1)] for _ in range(1,max(paper)[1]+11)]
background = [[0 for _ in range(101)] for _ in range(101)]
for i in range(len(paper)):
    x = paper[i][0]
    y = paper[i][1]
    for l in range(y, y+10):
        for w in range(x, x+10):
            background[l][w] = 1
s = 0
for i in background:
    s += sum(i)
    
print(s)