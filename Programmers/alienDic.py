# def solution(spell, dic):
#     isIn = False
    
#     for d in dic:
#         result = []
#         for s in spell:
#             #print(s, d)
#             result.append(True if s in d else False)
#         #print(result)
#         if False not in result:
#             return 1
#     return 2
#     # while d< len(dic):
    #     for s in spell:
    #         if s not in d:
                
    # isIn = [False] * len(spell)
    # for s in spell:
    #     for d in dic:
    #         if s in d:
    #             isIn = True
    #     if isIn == True:
    #         return 2
    # isIn = False
    # for d in dic:
    #     for s in spell:
    #         if s in d:
    #             isIn = True
    #         else:
    #             print(s)
    #             isIn = False

    #     if isIn :
    #         return 1
    # return 2
    # else:
    #     isIn = False
    # answer = 1 if isIn else 2

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        print(spell-set(s))
        if not spell-set(s):
            return 1
    return 2

spell =["s", "o", "m", "d"]
dic = ["moos", "dzx", "smm", "sunmmo", "som"]

print(solution(spell, dic))