# 숫자길이를 3배로 늘려서 비교
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
#================================================================
def solution(numbers):
    numbers = sorted([str(n) for n in numbers], reverse=True)
    numbers.sort(key=lambda x:tuple(x[i:i+1] if x[i:i+1] else x[0] for i in range(4))+(x[-1],), reverse=True)
    if numbers[0]=='0':
        return '0'
    return ''.join(numbers)

print(solution([90,908,89,898,10,101,1,8,9]))
# https://programmers.co.kr/learn/courses/30/lessons/42746
