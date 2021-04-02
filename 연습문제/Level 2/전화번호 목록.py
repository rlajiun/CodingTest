# 1차 시도: 효율성-시간초과로 실패
def solution(phone_book):
    answer = []
    for i, p in enumerate(phone_book):
        answer.append(p.startswith(tuple(phone_book[:i])))
        answer.append(p.startswith(tuple(phone_book[i+1:])))
    return not any(answer)

# 2차 시도: 효율성-시간초과 실패가 반으로 줄음
def solution(phone_book):
    for i, p in enumerate(phone_book):
        if p.startswith(tuple(phone_book[:i])):
            return False
        elif p.startswith(tuple(phone_book[i+1:])):
            return False
    return True

# 3차 시도
def solution(phone_book):
    phone_book.sort()
    for i, p in enumerate(phone_book):
        if p.startswith(tuple(phone_book[:i])):
            return False
    return True

# 4차 시도
def solution(phone_book):
    f = 'f'
    idx = 0
    phone_book.sort()
    for i, p in enumerate(phone_book):
        if not p.startswith(f):
            f = p
            idx = i
            continue
        elif p.startswith(tuple(phone_book[idx:i])):
            return False
    return True

# 해시로 푸는 법
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # temp in hash_map 은 hasp_map 딕셔너리에 temp가 키인 값이 있는 지 확인
            if temp in hash_map and temp != phone_number:
                return False
    return True

print(solution(["123", "1244", "125", "126", "127", "128"]))
# https://programmers.co.kr/learn/courses/30/lessons/42577
