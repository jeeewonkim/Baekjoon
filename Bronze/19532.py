import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())
#x =0; y =0
for x in range(-999, 1000):
    for y in range(-999,1000):
        if c == a*(x) + b*y and f == d*x + e*y:
            print(x,y)
            break
    



# if a == 0 :
#     if b != 0 :
#         y = c//b
#         x = (f-e*(y))//d if d!=0 else 0
#     # else:
#     #     y = 0
#     #     x = f//d if d!=0 else 0

# elif b == 0 :
#     if a !=0 :
#         x = c//a
#         y = (f-(d*x))//e if e!=0 else 0
#     # else:
#     #     x = 0
#     #     y = f//e if
        
# #f-> c , e->b, d->a
# if d == 0 :
#     if e != 0 :
#         y = f//e
#         x = (c-b*(y))//a if a!=0 else 0
#     # else:
#     #     y = 0
#     #     x = c//a if a!=0 else 0
# # b-> e a-> d c-> f
# elif e == 0 :
#     if d !=0 :
#         x = f//d
#         y = (c-(a*x))//b if b!=0 else 0
#     # else:
#     #     x = 0
        

        
# else:
#     q = ((b*(-1)*d)+a*e)
#     y = ((c*(-1*d))+(a*f))//q if q !=0 else 0
#     x = (c - b*(y))//a

# print(x,y)