def solution(picks, minerals):
    answer = 0
    minerals = minerals[:min(len(minerals), sum(picks)*5)]

    cnt_min = [[0,0,0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_min[i//5][0] += 1
        elif minerals[i] == "iron":
            cnt_min[i//5][1] += 1
        else:
            cnt_min[i//5][2] +=1
    cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))

    for mineral in cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:
                picks[p] -=1
                answer += d+i+s
                break
            if p ==1 and picks[p] > 0 :
                picks[p]-=1
                answer += 5*d +i + s
                break
            if p ==2 and picks[p] > 0:
                answer += 25*d + 5*i + s
    return answer