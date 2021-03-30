def solution(nums):
    return min(len(set(nums)), len(nums)//2)

# Counter 사용할 필요없음
from collections import Counter
def solution(nums):
    return min(len(Counter(nums)), len(nums)//2)

print(solution([3,1,2,3]))
# https://programmers.co.kr/learn/courses/30/lessons/1845
