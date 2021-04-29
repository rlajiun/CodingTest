def solution(s):
    answer = len(s)
    string = ''
    alpa = ''
    cnt = 0
    for i in range(1, len(s)//2+1):
        for j in range(0, len(s), i):
            if alpa == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 0:
                    if cnt == 1: string += alpa
                    else: string += str(cnt) + alpa
                alpa = s[j:j+i]
                cnt = 1
        if cnt != 0:
            if cnt == 1: string += alpa
            else: string += str(cnt)+alpa
            alpa = ''
            cnt = 1
            if answer > len(string):
                answer = len(string)
        string = ''

    return answer

print(solution("ababcdcdababcdcd"))
# https://programmers.co.kr/learn/courses/30/lessons/60057
