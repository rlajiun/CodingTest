arr = [1,1,3,3,0,1,1]
answer = []

answer.append(arr[0])
for a in arr:
  if answer[-1]!=a:
    answer.append(a)

print(answer) # [1,3,0,1]
