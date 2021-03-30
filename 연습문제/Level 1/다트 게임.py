# 3차 시도: 다른 사람의 풀이를 보고 더 깔끔하게 고쳐봄
import re
def solution(dartResult):
    domain = {'S':'1','D':'2','T':'3'}
    option = {'':'1','*':'2','#':'(-1)'}
    answer = '0'
    for i in re.findall('(\d+)([SDT])([*#]?)', dartResult):
        if '*' in i:
            answer += '*2' 
        answer += '+' + i[0] + '**' + domain[i[1]] + '*' + option[i[2]]
    return eval(answer)

# 다른 사람의 풀이
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 2차 시도: 정규표현식을 사용하여 통과
import re
def solution(dartResult):
    domain = {'S':'1','D':'2','T':'3'}
    answer = '0'
    for i in re.finditer('[0-9]+[a-zA-Z][*]?#?', dartResult):
        if re.search('[*]',i.group()):
            answer += '*2+' + i.group()[:-2] + '**' + domain[i.group()[-2]] + '*2'
        elif re.search('#',i.group()):
            answer += '+' + i.group()[:-2] + '**' + domain[i.group()[-2]] + '*(-1)'
        else:
            answer += '+' + i.group()[:-1] + '**' + domain[i.group()[-1]]
    return eval(answer)

# 1차 시도: 점수가 10인 경우를 고려하지 못해 실패
def solution(dartResult):
    score = []
    domain = {'S':'1','D':'2','T':'3'}
    answer = '0'
    for s in dartResult:
        if s.isdigit():
            score.append(" ")
        score.append(s)
    score = "".join(score).split()
    for s in score:
        print(answer)
        if len(s) < 3:
            answer += '+' + s[0]+'**'+ domain[s[1]]
        else:
            if s[2] == '*':
                answer += '*2+' + s[0] + '**' + domain[s[1]] + '*2'
            else:
                answer += '+' + s[0] + '**' + domain[s[1]] + '*(-1)'
    return eval(answer)

print(solution("10S2D*3T"))
# https://programmers.co.kr/learn/courses/30/lessons/17682
