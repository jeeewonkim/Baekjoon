s = [int(input()) for i in range(3)]
p= ""
if sum(s) == 180:
    for i in range(3):
        cnt = s.count(s[i])
        if cnt == 3 :
            p="Equilateral"
            break
        elif cnt == 2 :
            p ="Isosceles"
            break
        elif cnt == 1:
            p = "Scalene"
else:
    p = "Error"
    
print(p)