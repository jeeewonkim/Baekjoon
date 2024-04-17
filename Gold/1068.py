import sys
input = sys.stdin.readline

n = int(input())
node = list(map(int, input().split()))
tree = [[]for _ in range(n)]
for i in range(n):
    if node[i] != -1:
        tree[node[i]].append(i)
    else:
        root_node = i

def remove_tree(r):
    if tree[r]:
        for i in tree[r]:
            remove_tree(i)
            tree[r] = [-1]
    else:
        tree[r] = [-1]
        for i in range(n):
            if [r] == tree[i]:
                tree[i] = []
                break


r = int(input())

if root_node == r:
    print(0)
else:
    remove_tree(r)
    count = 0
    remove_count = 0
    for i in range(n):
        if not tree[i]:
            count += 1
        elif tree[i] == [-1]:
            remove_count +=1
    if remove_count == n-1 and count == 0:
        count = 1

    print(count)






