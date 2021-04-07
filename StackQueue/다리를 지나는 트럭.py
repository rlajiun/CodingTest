# 1차 시도: 시간 초과
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    for t in truck_weights:
        while weight - t < 0:
            weight += bridge.popleft()
            if weight - t >= 0: break
            bridge.append(0)
            answer += 1
        weight -= t
        bridge.append(t)
        answer += 1
    
    if bridge:
        answer += len(bridge)

    return answer

# 2차 시도
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    while len(bridge) != 0:
        out = bridge.popleft()
        weight += out
        answer += 1
        if truck_weights:
            if weight - truck_weights[0] >= 0:
                left = truck_weights.popleft()
                weight -= left
                bridge.append(left)
            else:
                bridge.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))
# https://programmers.co.kr/learn/courses/30/lessons/42583
