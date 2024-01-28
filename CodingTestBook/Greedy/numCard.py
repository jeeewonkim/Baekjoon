#숫자 카드 게임
n, m = map(int,input().split())
card = []
for i in range(n):
    c = list(map(int, input().split()))
    card.append(min(c))
print(max(card))
