from collections import deque
import re
def solution(expression):
    answer = []
    operator = deque(['+', '-', '*'])
    operator2 = deque(['*', '-','+'])
    expr = re.split('(\D+)', expression)
    oper(operator, expr, answer)
    oper(operator2, expr, answer)
    return max(answer)

def oper(operator, expr, answer):
    for r in range(3):
        expr2 = expr[:]
        for op in operator:
            while op in expr2:
                i = expr2.index(op)
                expr2[i-1:i+2] = [str(eval(''.join(expr2[i-1:i+2])))]
        answer.append(abs(int(expr2[0])))
        operator.append(operator.popleft())

print(solution("100-200*300-500+20"))
# https://programmers.co.kr/learn/courses/30/lessons/67257
