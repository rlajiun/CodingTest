def solution(n, arr1, arr2):
  answer = []
  for i in range(n):
    string = format(arr1[i]|arr2[i], '0'+str(n)+'b')
    string = string.replace('0',' ')
    string = string.replace('1', '#')
    answer.append(string)
  return answer
======================================================
def solution(n, arr1, arr2):
  arr1 = [format(i, '0'+str(n)+'b') for i in arr1]
  arr2 = [format(i, '0'+str(n)+'b') for i in arr2]
  answer = []
  for i in range(n):
    string = ''
    for j in range(n):
      if arr1[i][j] == arr2[i][j] == '0':
        string+=" "
      else:
        string+="#"
    answer.append(string)
  return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
# https://programmers.co.kr/learn/courses/30/lessons/17681
