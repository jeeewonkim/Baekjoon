h,m = map(int, input().split())
timer = int(input())

m+=timer
while(m>0):
    if m >= 60:
        m -= 60
        h += 1
        if h==24:
            h = 0
    else: break
print(h,m)