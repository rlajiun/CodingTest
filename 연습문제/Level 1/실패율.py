def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
=============================================================
from collections import Counter

def solution(N, stages):
  stop = Counter(stages) # 정체하고 있는 수
  reach = [] # 도달한 수
  fail = {} # stop / reach
  x = 0
  for i in range(N+1, 0, -1):
    x += stop[i]
    reach.append(x) # 반대로 입력
  
  for i,j in enumerate(reach[::-1]):
    if j==0:
      fail[i+1] = 0
    else:
      fail[i+1] = stop[i+1]/j
  del fail[N+1]
  fail = sorted(fail.items(), key=lambda x:x[1], reverse=True)
  return [x for x,y in fail]
print(solution(4,[4,4,4,4,4]))
# https://programmers.co.kr/learn/courses/30/lessons/42889
