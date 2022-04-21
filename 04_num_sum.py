# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 푼방법1
# def solution(a, b):
#     answer = 0
#     if(a > b):
#         for num in range(b, a+1):
#             answer += num
#         return answer
#     else: 
#         for num in range(a, b+1):
#             answer += num  
#         return answer

# 푼방법2
# def solution(a, b):
#   return a if a == b else sum(range(min(a,b), max(a,b)+1))

# 다른 풀이 참고 방법3
# def solution(a, b):
#     if a > b: a, b = b, a
#     return sum(range(a,b+1))

# 다른 풀이 참고 방법4 (시간복잡도 O(1))
# 사각형 반띵한 것의 넓이라고 생각.
def solution(a, b):
  return (abs(a-b) + 1) * (a+b) / 2

a = 5
b = 3
solution(a, b)