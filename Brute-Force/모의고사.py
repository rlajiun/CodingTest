def solution(answers):
    score = [0, 0, 0]
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, i in enumerate(answers):
        if p1[idx % 5] == i:
            score[0] += 1
        if p2[idx % 8] == i:
            score[1] += 1
        if p3[idx % 10] == i:
            score[2] += 1

    scoreMax=max(score)
    for s in range(len(score)):
        if score[s]==scoreMax:
            answer.append(s+1)
    answer.sort()
    return answer
