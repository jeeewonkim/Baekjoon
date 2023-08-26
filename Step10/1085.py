x,y,w,h = map(int,input().split())
a = x if x<abs(w-x) else abs(w-x)
b = y if y<abs(h-y) else abs(h-y)
print(a if a<b else b)