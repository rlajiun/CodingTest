def solution(priorities, location):
    answer = 0
    while location >= 0:
        maxp = max(priorities)
        p = priorities.pop(0)
        if p < maxp:
            priorities.append(p)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
        else:
            answer += 1
            location -= 1
    return answer

print(solution([1], 0))
# https://programmers.co.kr/learn/courses/30/lessons/42587
