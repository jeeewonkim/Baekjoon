n, k =  map(int,input().split())
score = list(map(int, input().split()))
s_score = sorted(score)

print(s_score[-k])