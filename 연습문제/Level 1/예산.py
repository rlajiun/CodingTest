def solution(d, budget):
    answer = 0
    d.sort()
    cnt = 0
    for i in d:
        if answer + i > budget: break
        else:
            answer += i
            cnt += 1
    return cnt

print(solution([1,3,2,5,4], 9))
#https://programmers.co.kr/learn/courses/30/lessons/12982
