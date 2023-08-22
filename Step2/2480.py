dice = list(map(int, input().split()))
count =0
diceNum = 0
for i in range(len(dice)-1):
    for j in range(i+1,3):
        if dice[i] == dice[j]:
            count = dice.count(dice[i])
            diceNum = dice[i]
if count == 3:
    print(10000+diceNum*1000)
if count == 2:
    print(1000+ diceNum *100)
if count == 0:
    print(max(dice)*100)
    