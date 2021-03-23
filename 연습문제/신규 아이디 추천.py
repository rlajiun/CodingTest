import re

# new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "=.="

# 1단계: 모든 대문자를 소문자로 치환
new_id = new_id.lower()

# 2단계: 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
new_id = re.sub("[^0-9a-z-_.]","",new_id)

# 3단계: .가 2번 이상 연속된 부분을 하나의 .로 치환
new_id = re.sub("[.]{2,}",".",new_id)

# 4단계: .가 처음이나 끝에 위치한다면 제거
new_id = re.sub("^[.]|[.]$","",new_id)

# 5단계: 빈문자열이라면 "a"대입
if len(new_id) == 0: new_id = "a"

# 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
if len(new_id) >= 16:
  new_id = new_id[:15]
  new_id = re.sub("^[.]|[.]$","",new_id)

# 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
if len(new_id) <= 2:
  for c in range(3,len(new_id),-1):
    new_id+=new_id[-1]

print(new_id)
