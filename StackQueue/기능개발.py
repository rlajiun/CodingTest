def solution(progresses, speeds):
    answer = []
    while progresses:
        while progresses[0] < 100:
            progresses = [x+y for x , y in zip(progresses, speeds)]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
# https://programmers.co.kr/learn/courses/30/lessons/42586
