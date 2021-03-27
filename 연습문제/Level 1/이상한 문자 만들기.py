def solution(s):
    answer = []
    for word in s.split(" "):
        new = ''
        for w in range(len(word)):
            if w%2==0:
                new += word[w].upper()
            else:
                new += word[w].lower()
        answer.append(new)
    return " ".join(answer)
