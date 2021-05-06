def solution(s):
    stack = []
    for i in s:
      if stack:
        last = stack.pop()
        if last != i:
          stack.extend([last, i])
      else:
        stack.append(i)
    
    return 0 if stack else 1

print(solution("cdcd"))
# https://programmers.co.kr/learn/courses/30/lessons/12973
