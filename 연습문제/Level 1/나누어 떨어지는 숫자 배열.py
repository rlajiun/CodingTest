arr = [2, 36, 1, 3]
divisor = 1
answer = []

for i in arr:
  if i % divisor == 0:
    answer.append(i)

if len(answer) == 0:
  answer.append(-1)
else:
  answer.sort()

print(answer) # [1, 2, 3, 36]
