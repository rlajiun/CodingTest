import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

print(solution(8, 12))
# https://programmers.co.kr/learn/courses/30/lessons/62048
