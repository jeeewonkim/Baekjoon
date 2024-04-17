# num = []
# #1666-5666
# for i in range(1,6):
#     num.append(str(i)+'666')
# #6661-6669
# for i in range(1,10):
#     num.append('666'+str(i))
# for i in range(7,16):
#     num.append(str(i) + '666')
# for i in range(1,10):
#     num.append('1666'+str(i))


import sys
num = []
n = int(sys.stdin.readline())

for i in range(666,10000000):
    if '666' in str(i):
        num.append(i)
        
print(num[n-1])