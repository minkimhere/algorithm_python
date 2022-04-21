# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 푼 방법1
# def solution(numbers):
#     answer = 0
#     numsum = sum(range(0, 10))
    
#     for _ in numbers:
#         answer += _
#     answer = numsum - answer
#     return answer
  
# 다른 풀이 참고 방법2
# def solution(numbers):
#   return sum(range(0,10)) - sum(numbers)

# 다른 풀이 참고 방법2
# def solution(numbers):
#   return sum(set(range(1,10)) - set(numbers))

# 다른 풀이 참고 방법3
def solution(numbers):
  answer = 0
  for num in range(1,10):
    if num not in numbers: answer += num
  print(answer)

numbers = [1,2,3,4,5,6,7,8,0]
solution(numbers)