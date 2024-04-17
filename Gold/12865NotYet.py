import sys

input = sys.stdin.readline

N, K = map(int, input().split())

weight, value = [], []

for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

nums = [i for i in range(N)]
answer_list = []


def combi(n, ans, w_sum, v_sum):
    if n == N:
        if w_sum == K:
            answer_list.append(v_sum)
        return
    ans.append(nums[n])
    combi(n + 1, ans, w_sum + weight[n], v_sum + value[n])
    ans.pop()
    combi(n + 1, ans, w_sum, v_sum)

ans = []
combi(0, ans, 0, 0)

print(max(answer_list))