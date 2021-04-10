def solution(citations):
    answer = {}
    for i in range(len(citations)+1):
        answer.update({i:len([x for x in citations if x >= i])})
    return max([x for x, y in answer.items() if x<=y])

print(solution([10,11,12,13]))
# https://programmers.co.kr/learn/courses/30/lessons/42747
