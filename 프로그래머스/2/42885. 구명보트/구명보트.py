from collections import *
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    boat = 0
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        boat+=1


    if people:
        boat +=1
    return boat
