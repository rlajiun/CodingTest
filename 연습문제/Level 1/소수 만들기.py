# 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수
def solution(nums):
    sumNums = []
    nums.sort()
    # 서로 다른 3개를 골라 더한 값 구하기
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sumNums.append(nums[i]+nums[j]+nums[k])

    # 소수 구하기
    prime = set(range(2,sumNums[-1]+1))
    for i in range(2,sumNums[-1]+1):
        if i in prime:
            prime -= set(range(2*i, sumNums[-1]+1, i))

    sumNums = [x for x in sumNums if x in prime]
    return len(sumNums)

print(solution([1,2,3,4]))
# https://programmers.co.kr/learn/courses/30/lessons/12977
