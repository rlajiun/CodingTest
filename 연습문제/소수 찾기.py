# 다른 사람의 풀이에서 본 간결한 코드
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

=============================================================================================================

import math
# 소수 판별 함수(에라토스테네스의 체)
def solution(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return len([ i for i in range(2, n+1) if array[i] ])
  
==============================================================================================================

# 효율성 실패(시간 초과)
def solution(n):
    prime = [2]
    for i in range(2,n+1):
        for j in prime:
            if i % j == 0: # 소수가 아닐때
                break
            elif j == prime[-1]:
                prime.append(i)
    return len(prime)
    return answer
