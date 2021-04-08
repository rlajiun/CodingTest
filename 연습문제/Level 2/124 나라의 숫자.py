def solution(n):
    answer = ''
    num = ['1','2','4']
    i = 1
    while n > 3**i:
        n -= 3**i
        i += 1

    for x in range(i,0,-1):
        j = 0
        while n > 3**(x-1):
            n -= 3**(x-1)
            j += 1
        answer += num[j]
    return answer

print(solution(4))
# https://programmers.co.kr/learn/courses/30/lessons/12899
