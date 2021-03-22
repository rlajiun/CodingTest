a = 5
b = 24
answer = ''
DAYS = ('FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU')
DATE = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# 처음 풀이
# mon = 0
# for i in range(a-1):
#     mon += DATE[i]
# answer = DAYS[(mon+b) % 7 - 1]

# sum 함수를 사용하니 더 간단함
answer = DAYS[(sum(DATE[:a-1])+b) % 7 -1]

print(answer) # TUE
