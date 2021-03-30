def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    h = {'L': 10,'R': 12}
    for i in numbers:
        if i == 0: i = 11
        lCnt = sum(divmod(abs(h['L']-i),3))
        rCnt = sum(divmod(abs(h['R']-i),3))
        if i in right or (i not in left and lCnt > rCnt):
            answer += 'R'
            h['R'] = i
        elif i in left or (i not in right and lCnt < rCnt):
            answer += 'L'
            h['L'] = i
        else:
            answer += hand[0].upper()
            h[hand[0].upper()] = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# https://programmers.co.kr/learn/courses/30/lessons/67256
