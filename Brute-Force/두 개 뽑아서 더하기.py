def solution(numbers):
    answer = []

    for num, i in enumerate(numbers):
        for j in range(num+1, len(numbers)):
            answer.append(i+numbers[j])

    answer = sorted(list(set(answer)))

    return answer
