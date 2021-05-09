def solution(s):
    num = tuple(map(int, s.split()))
    return str(min(num)) + ' ' + str(max(num))

print(solution("1 2 3 4"))
# https://programmers.co.kr/learn/courses/30/lessons/12939
