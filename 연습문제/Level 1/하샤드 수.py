def solution(arr):
  return arr % sum([int(c) for c in str(arr)]) == 0

==========================================================

from functools import reduce

def solution(arr):
    if arr % int(reduce(lambda x, y: int(x) + int(y), str(arr))) == 0:
        return True
    return False

print(solution(1))
#https://programmers.co.kr/learn/courses/30/lessons/12947
