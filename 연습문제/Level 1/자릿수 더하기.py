def solution(n):
    answer = 0

    for i in range(len(str(n))-1, -1, -1):
      answer += n//(10**i)
      n -= n//(10**i)*(10**i)

    return answer
