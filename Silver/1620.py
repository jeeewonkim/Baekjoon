import sys

n, m = map(int, sys.stdin.readline().split())

# dogam_num = {i:sys.stdin.readline().strip() for i in range(1,n+1)}
# dogam_name ={sys.stdin.readline().strip() : i for i in range(1, n+1)}
dogam_num = {}
dogam_name = {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    dogam_num[i] = name
    dogam_name[name] = i
    

for i in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(dogam_num[int(q)])
    else:
        print(dogam_name[q])
    # for key, val in dogam.items():
    #     if val == q :
    #         print(key)
    #         break
    #     elif key == q:
    #         print(val)
    #         break
    # if not q.isnumeric():
    #     for key, val in dogam.items():
    #         if val == q:
    #             print(key)
    #             break
    # else:
    #     print(dogam[int(q)])
        # if q.isnumeric() and int(q) == key:
        #     print(val)
        #     break
        # elif q.isnumeric()==False and q == val:
        #     print("!!")
        #     print(key)
        #     break
        # if q == val :
        #     print(key)
        # if q == key :
        #     print(val)
    # if type(q) == str:
        