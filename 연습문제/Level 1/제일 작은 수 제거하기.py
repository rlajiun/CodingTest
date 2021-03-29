def solution(arr):
  return [i for i in arr if i > min(arr)]
==========================================================
def solution(arr):
    min = arr[0]
    for i in arr:
      if i < min: min = i
    arr.remove(min)
    if len(arr)==0: return [-1]
    return arr

print(solution([10]))
#https://programmers.co.kr/learn/courses/30/lessons/12935
