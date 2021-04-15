import math
def solution(brown, yellow):
    answer = []
    x_plus_y = brown//2+2
    xy = brown+yellow
    for i in range(1, math.ceil(xy**0.5)+1):
        if xy % i == 0 and xy//i + i == x_plus_y:
            answer.extend([xy//i, i])
            break
    return answer

print(solution(10,2))
# https://programmers.co.kr/learn/courses/30/lessons/42842
