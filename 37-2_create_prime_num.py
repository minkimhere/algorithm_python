# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.



# 방법1
# def check(a, b, c):
#     numSum = a + b + c
#     for i in range(2, numSum):
#         if numSum % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if check(nums[i], nums[j], nums[k]):
#                     answer += 1
#     return answer

# 소수 검사할 때 그 수의 약수 앞에 부분만 돌기
# 1 2 4 8 16 이렇게 됐을 때 (1,16) (4,4))(2,9) 이런식으로 어차피 앞부분 하나만 검사해도 쌍으로 되기 때문
# def check(a, b, c):
#     numSum = a + b + c
#     for i in range(2, int(numSum**0.5)+1):
#         if numSum % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if check(nums[i], nums[j], nums[k]):
#                     answer += 1
#     return answer


# 방법2
# itertools의 combinations라는 메소드 사용하기
# https://eda-ai-lab.tistory.com/493
# combination() 사용 : 중복을 허용하지 않고, 순서 의미가 있는 조합을 리턴해준다.
from itertools import combinations

def check(a, b, c):
    numSum = a + b + c
    for i in range(2, int(numSum**0.5)+1):
        if numSum % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    threeNums = list(combinations(nums, 3))
    for threeNum in threeNums:
        if check(threeNum[0], threeNum[1], threeNum[2]):
            answer += 1
    return answer

nums = [1,2,3,4]
# nums = [1,2,7,6,4]
solution(nums)