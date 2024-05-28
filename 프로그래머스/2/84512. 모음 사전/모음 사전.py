from itertools import permutations


def solution(word):
    words = ['A'] * 5 + ['E'] * 5 + ['I'] * 5 + ['O'] * 5 + ['U'] * 5
    combi = set()
    for i in range(1, 6):
        for p in permutations(words, i):
            combi.add(''.join(p))

    combi = sorted(combi)

    for c in range(len(combi)):
        if combi[c] == word:
            return c+1
