import sys

input = sys.stdin.readline


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]


# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a

    elif b in know_truth:
        parent[a] = b

    else:
        if a < b:
            parent[b] = a

        else:
            parent[a] = b


n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n + 1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(parent, party[i], party[i + 1], know_truth)

    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know_truth:
            break

    else:
        ans += 1

print(ans)
# truth = list(map(int, input().split()))
# party = []
# people = [False] * (n + 1)  # 초기에 모든 사람을 거짓말쟁이로 설정
#
# for i in range(m):
#     party.append(list(map(int, input().split()))[1:])  # 파티에 오는 사람의 번호만 리스트에 추가
#     for j in truth[1:]:
#         if j in party[i]:
#             for k in party[i]:
#                 people[k] = True  # 진실을 아는 사람은 거짓말을 할 수 없음
#             break
#
# count = 0
#
# for p in party:
#     for i in p:
#         if people[i]:
#             break
#     else:
#         count += 1
#
# print(count)
# for i in range(m):
#     party.append(list(map(int,input().split()))[1:])
#     for j in truth[1:]:
#         if j in party[i]:
#             for k in party[i]:
#                 people[k] = True
#             break
#
# count = 0
#
# if len(truth) == 1 or True not in people[1:]:
#     print(m)
#
# else:
#     if False not in people[1:]:
#         print(0)
#
#     else:
#         for p in party:
#             for i in p:
#                 if people[i] == True:
#                     break
#             else:
#                 count +=1
#
#         print(count)

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# truth = list(map(int,input().split()))[1:]  # 진실을 아는 사람의 번호를 set으로 변환
# party = []
# for _ in range(m):
#     party.append(list(map(int,input().split()))[1:])
# count = 0
#
# for _ in range(m):  # 각 파티에 대해 반복
#     for p in party:
#         if truth.isdisjoint(p):  # 파티 참석자와 진실을 아는 사람의 집합이 겹치지 않는 경우
#             count += 1
#             break
#
# print(count)