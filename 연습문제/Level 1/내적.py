def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

print(solution([-1,0,1],[1,0,-1]))
# https://programmers.co.kr/learn/courses/30/lessons/70128
