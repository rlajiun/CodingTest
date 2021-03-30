def solution(n):
    answer = ''
    while n > 0:
        answer += str(n % 3)
        n = n // 3
    return int(answer,3)

print(solution(45))
# https://programmers.co.kr/learn/courses/30/lessons/68935
