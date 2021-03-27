def solution(s, n):
    answer = ''
    up = [i for i in range(65,91)]
    lo = [i for i in range(97,123)]

    for i in s:
        if ord(i) in up:
            if ord(i)+n>up[-1]:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        elif ord(i) in lo:
            if ord(i)+n>lo[-1]:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        else:
            answer += i
    return answer
