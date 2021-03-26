def solution(n):
    answer = [int(i) for i in list(str(n))] # list(str(n))은 그냥 str(n)으로 해도 list로 만들어짐
    answer.reverse()

    return answer
