participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = ''

# 효율성 탈락 - 시간 초과
# 이유를 찾아보니까
# i가 인덱스가 아니라 항목 값이라서 remove(i)를 하면 O(n)가
# for문 안에 들어있으니 O(n^2)이 됨
for i in completion:
    participant.remove(i)
answer = participant[0]

# 해결법
# 삭제는 해시맵을 제외하고 대부분의 자료구조가 O(n)이 걸림
# 빠르게 삭제하기 위해선 해시맵을 사용해야 함 -> 파이썬은 딕셔너리
# 삭제를 하지 않고 정렬해서 찾음
participant.sort()
completion.sort()
answer = participant[len(participant)-1]
for i in range(len(completion)):
    if participant[i] != completion[i]:
        answer = participant[i]
        break
        
# 해시 키 값을 이용한 풀이 방법
temp = 0
dic = {}
for part in participant:
    dic[hash(part)] = part
    temp += hash(part)
for com in completion:
    temp -= hash(com)
answer = dic[temp]

print(answer)
