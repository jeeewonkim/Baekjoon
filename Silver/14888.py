#연산자 끼워넣기
import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
oper = []

def cal(a,b,o):
    if o == 0:
        return a+b
    if o == 1:
        return a-b
    if o ==2:
        return a*b
    if o == 3:
        if a < 0 :
            return -(abs(a)//b)
        else:
            return a//b
for i in range(4):
    for j in range(op[i]):
        oper.append(i)
        
oper_r = []
rst = []
def back():
    if len(rst) == n-1:
        oper_r.append(list(oper[i] for i in rst))
        return
    
    for i in range(len(oper)):
        if i not in rst:
            rst.append(i)
            back()
            rst.pop()
back()
r_list = []

for i in oper_r:
    r = num[0]
    for j in range(n-1):
        r = cal(r, num[j+1], i[j])
    r_list.append(r)
    
print(max(r_list))
print(min(r_list))
