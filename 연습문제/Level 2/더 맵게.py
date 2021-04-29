# 2차 시도: heapq 사용 -  통과
import heapq
def solution(scovile, K):
    heapq.heapify(scovile)
    answer = 0
    while scovile:
        try:
            min = heapq.heappop(scovile)
            if min < K:
                mix = min + (heapq.heappop(scovile)*2)
                heapq.heappush(scovile, mix)
                answer += 1
        except:
            return -1
    return answer

# 1차 시도: 정확성: 33.3 효율성: 0.0
from collections import deque
def solution(scoville, K):
    answer = 0
    scoville = deque(sorted(scoville))
    print(scoville)
    while scoville[0] < K:
        try:
            mix = scoville.popleft()+(scoville.popleft()*2)
            if scoville:
                for i, s in enumerate(list(scoville)):
                    if s >= mix:
                        scoville.insert(i, mix)
                        print(scoville)
                        break
            else:
                scoville.append(mix)
            answer += 1
        except:
            return -1
    return answer

print(solution([2, 3, 9, 10, 1, 12], 7))
# https://programmers.co.kr/learn/courses/30/lessons/42626
