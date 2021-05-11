from collections import deque
def solution(skill, skill_trees):
    answer = len(skill_trees)
    for t in skill_trees:
      queue = deque([x for x in skill])
      for s in t:
        if s in skill and queue:
          if s == queue[0]:
            queue.popleft()
          else: 
            answer -= 1
            break
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# https://programmers.co.kr/learn/courses/30/lessons/49993
