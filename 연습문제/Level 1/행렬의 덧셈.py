def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a = []
        for j in range(len(arr1[i])):
            a.append(arr1[i][j] + arr2[i][j])
        answer.append(a)
        # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)] 다른 사람의 풀이
    return answer
