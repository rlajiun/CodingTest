def solution(n):
  sqrt = n**0.5
  if sqrt % 1 == 0:
    return (sqrt+1)**2
  return -1
=============================================================
import math
def solution(n):
    if math.sqrt(n)%1 == 0:
      return pow(math.sqrt(n)+1,2)
    else:
      return -1

print(solution(121))
# https://programmers.co.kr/learn/courses/30/lessons/12934
