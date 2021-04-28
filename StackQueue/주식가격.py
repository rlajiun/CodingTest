def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i, p in enumerate(prices):
        for n in stack:
            answer[n] += 1
        while stack and prices[stack[-1]] > p:
            stack.pop()
        stack.append(i)
    return answer

print(solution([1, 2, 3, 2, 3]))
# https://programmers.co.kr/learn/courses/30/lessons/42584
