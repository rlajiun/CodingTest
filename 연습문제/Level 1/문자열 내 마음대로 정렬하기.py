strings = ["abce", "abcd", "cdx"]
n = 2
answer = []
strings.sort()
c = sorted([[s[n], i] for i, s in enumerate(strings)])
for i in c:
    answer.append(strings[i[1]])
print(answer)

===============================================================

print(sorted(sorted(strings), key=lambda x: x[n]))
