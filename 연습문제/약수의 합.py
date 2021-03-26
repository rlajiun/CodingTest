# 다른 사람의 풀이: 반 넘는 값은 검사할 필요가 없음
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

============================

def solution(n):
    divisor = set()

    for i in range(1, n+1):
      if n % i == 0:
        divisor.add(n//i)
        divisor.add(i)
    return sum(divisor)
