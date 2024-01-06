#동서남북 갈 수 있는 칸의 개수
from math import prod

n, m = map(int,input().split())
x,y,d = map(int, input().split())

mp = [list(map(int, input().split()))for _ in range(m)]
mp[y][x] = 2
mv =[]
# 0 : 북쪽, 1 : 동쪽, 2: 남쪽, 3: 서쪽

#1. 범위 안에 있어야함 
#2. 이동하면 향하는 방향이 바뀜 d =(d+3)%4
count = 0
for j in range(m):
    for i in range(4):
        mv = [mp[y-1][x],mp[y][x+1], mp[y+1][x], mp[y][x-1]]
        if(prod(mv)==1): # 사방면이 바다일 때
            break
        elif sum(mv)>4:
                #d = (d+2)%4
                print("d: ",mv[d], x, y)
                if mv[(d+2)%4] == 1:
                    break
                else:
                    if d == 0 and y!=3: #북을 바라보고 남으로 이동
                        y+=1
                        # print("북으로 이동")
                    elif d==1 and x!=0: #동을 바라보고 서로 이동
                        x-=1
                        # print("동으로 이동")
                    elif d==2 and y!=0: #남을 바라보고 북으로 이동
                        y-=1
                        # print("남으로 이동")
                    elif d==3 and x!= 3: #서
                        x+=1
                        # print("서로 이동")
                    mp[y][x] = 2
                    count+=1
        else: 
            d = (d+3)%4
            if mv[d]== 0:
                if d == 0 and y!=0: #북
                    y-=1
                elif d==1 and x!=3: #동
                    x+=1
                elif d==2 and y!=3: #남
                    y+=1
                elif d==3 and x!= 0: #서
                    x-=1
                mp[y][x] =2
                count +=1
                
                
            # elif sum(mv)>4:
            #     d = (d+2)%4
            #     if mv[d] == 1:
            #         break
            #     else:
            #         if d == 0 and y!=3:
            #             y+=1
            #         elif d==1 and x!=0:
            #             x-=1
            #         elif d==2 and y!=0:
            #             y-=1
            #         elif d==3 and x!= 3:
            #             x+=1
            #     mp[y][x] = 2
                
            
                #count +=1
        # if d == 0:
        #     if map_list[y-1][x] == 0: 
        #         y -=1
        #         map_list[y][x] = 1
        #         count +=1 
        # elif d == 1:
        #     if map_list[y][x+1] == 0:
        #         x +=1
        #         map_list[y][x] =1
        #         count +=1
                
        # elif d == 2:
        #     if map_list[y+1][x] == 0 :
        #         y +=1
        #         map_list[y][x] =1
        #         count +=1
                    
        # elif d == 3:
        #     if map_list[y][x-1] == 0:
        #         x-=1
        #         map_list[y][x] = 1
        #         count +=1
        
       # print("현재위치" , x, y)
print(count)