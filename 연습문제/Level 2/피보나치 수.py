import sys
def solution(n):
    return fibonacci(n) % 1234567

fibo = {0:0, 1:1}
def fibonacci(n):
    sys.setrecursionlimit(10**7)
    if n not in fibo:
        fibo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibo[n]

print(solution(9999))
# https://programmers.co.kr/learn/courses/30/lessons/12945
