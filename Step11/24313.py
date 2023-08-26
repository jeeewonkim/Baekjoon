a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
if a1*n0+a0 <= c*n0 and a1-c<=0:
    print(1)
else:
    print(0)
    
#(a1-c)*n+a0<=0의 조건일 때 a1-c가 양수일경우 무조건 성립 하지 않기 때문에 .. 