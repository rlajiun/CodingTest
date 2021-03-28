def solution(phone_number):
    return "*" * (len(phone_number)-4) + s[-4:]

==============================================================
# replace할 필요가 없었음
def solution(phone_number):
    return phone_number.replace(phone_number[0:-4],"*"*len(phone_number[0:-4]))

print(solution("01033334444"))
#https://programmers.co.kr/learn/courses/30/lessons/12948
