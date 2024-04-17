from itertools import permutations
def solution(a, b, g, s, w, t):
    answer = -1
    city = len(g)
    # per = permutations([i for i in range(city)], city)
    ef = {i : w[i]/t[i] for i in range(city)}
    #효율적인 도시부터
    ef = dict(sorted(ef.items(), key = lambda item: item[1], reverse = True))
    time = 0
    while True:
        for i in ef.keys():
            gold = min(w[i], g[i]) 
            silver =min(w[i]-gold ,s[i])
            a-=gold * (a//gold)
            b-=silver * (b//silver)
            print(a,b)
            time += t[i]
            # if a > 0 and b > 0:
            #     a -=g[i]
            #     b-= s[i]
            # if a> 0 and b<= 0:
            #     b-=s[i]
            if a <= 0 and b <= 0:
                return time
        else:
            time = 2*time
            
# def gold (a,g,w,t,i) :
#     a-=g[i]
#     return a
    
# def Silver(b,g,w,t,i):
#     b-=s[i]
    
    # for p in per:
    #     for i in p:
    #         if a > 0:
    #             gold = min(w[i], g[i])
    #             a -= gold
    #             Silver = min(w[i]- gold, s[i])
    #             b -= Silver
            
    return answer
# a,b,g,s,w,t = 10,10,[100],[100],[7],[10]
a,b,g,s,w,t = 90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]

print(solution(a,b,g,s,w,t))