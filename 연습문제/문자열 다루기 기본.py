s = "12345"
answer = True

if not len(s) == (4 or 6):
  answer = False
elif not s.isdigit():
  answer = False

print(answer) # False
