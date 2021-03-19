def solution(board, moves):
    answer = 0
    stack=[]
    for i in moves:
        i -= 1
        for j in board:
            if not j[i] == 0:
                stack.append(j[i])
                j[i] = 0
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        answer += 2
                        stack.pop()
                        stack.pop()
                break
    return answer
