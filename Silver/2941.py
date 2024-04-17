cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()

for i in cro:
       if i in s:
            a = s.count(i)
            s = s.replace(i,"1",a)
print(len(s))