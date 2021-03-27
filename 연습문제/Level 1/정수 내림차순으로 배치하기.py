def solution(n):
    return int("".join(sorted(str(n), reverse=True)))
  # sorted 할땐 str를 list()로 감싸지 않아도 됨
