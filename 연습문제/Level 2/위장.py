# 2차 시도: 의상 종류 중 입지 않았을 경우 +1을 해서 다 곱해준 후 다 입지 않았을 경우 -1을 해준다
from typing import Counter
def solution(clothes):
    answer = 1
    types = Counter(dict(clothes).values())
    for x in types.values():
        answer *= x+1
    return answer-1
  
# 1차 시도: 모든 경우를 비교하는라 시간 초과가 발생
from itertools import combinations
def solution(clothes):
    answer = 0
    for i in range(1, len(clothes)+1):
        for j in combinations(clothes,i):
            j = dict(j).values()
            print(j)
            if len(j) == len(set(j)):
                answer += 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# https://programmers.co.kr/learn/courses/30/lessons/42578
