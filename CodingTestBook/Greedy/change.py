#거스름돈

n = 1260
count = 0
coin = [500, 100, 50, 10]
for i in coin:
    count+= int(n/i)
    n%=int(n/i)*i
print(count)
    
