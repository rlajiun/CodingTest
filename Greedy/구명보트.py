# 2차 시도
from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people) > 1:
        if people[0]+people[-1] <= limit:
            people.pop()
        people.popleft()
        answer += 1
    return answer + len(people)

# 1차 시도: 효율성 실패 - 시간 초과
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    while len(people) > 1:
        if people[0]+people[-1] <= limit:
            people.pop(-1)
        people.pop(0)
        answer += 1
    return answer + len(people)

print(solution([70, 50, 80], 100))
# https://programmers.co.kr/learn/courses/30/lessons/42885
