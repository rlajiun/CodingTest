# 탐욕법(Greedy) 문제

n = 5 # 전체 학생의 수
lost = [1, 2, 3] # 체육복을 도난당한 학생들의 번호가 담긴 배열
reserve = [2, 3, 4] # 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
answer = n # 체육수업을 들을 수 있는 학생의 최댓값

for i in range(1, n+1):
    if i in lost:
        if i in reserve:
            # 남은 자신의 여벌의 체육복 쓰기
            reserve.remove(i)
        elif i-1 in reserve:
            # 앞에서 빌리기
            reserve.remove(i-1)
        elif i+1 in reserve and i+1 not in lost:
            # 뒤에서 빌리기
            reserve.remove(i+1)
        else:
            answer -= 1 # 못 빌릴 경우

print(answer)
