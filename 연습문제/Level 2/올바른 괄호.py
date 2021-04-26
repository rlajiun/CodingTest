def solution(s):
    answer = True
    s = [x for x in s]
    _str = {']':'[','}':'{',')':'('}
    dict_str = {'[':0,'{':0,'(':0}
    for j in s:
        try:
            dict_str[j] += 1
        except:
            dict_str[_str[j]] -= 1
            if dict_str[_str[j]] < 0:
                answer = False
                break
    if list(dict_str.values()) != [0]*3:
        answer = False
    return answer

print(solution("()()"))
# https://programmers.co.kr/learn/courses/30/lessons/12909
