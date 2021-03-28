arr = [1,1,3,3,0,1,1]
answer = []

answer.append(arr[0])
for a in arr:
  if answer[-1]!=a: # answer[-1:] != [a] 로 하면 answer이 빈 리스트여도 오류가 발생하지 않음
    answer.append(a)

print(answer) # [1,3,0,1]
