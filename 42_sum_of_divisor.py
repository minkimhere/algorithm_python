# 프로그래머스 약수의 합 https://programmers.co.kr/learn/courses/30/lessons/12928

#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.


# 푼 방법1
# def solution(n):
#     answer = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer.append(i)
#     return sum(answer)


# 푼 방법2
# def solution(n):
#     return sum([i for i in range(1, n+1) if n % i == 0])

  
# 방법3
# def solution(n):
#     return sum(filter(lambda x: n % x == 0, range(1, n+1)))

  
# 방법4
# 어차피 자기 자신은 약수이고, 자기 자신 바로 전 약수는 2로 나눈 값이다. 그러므로 반 나눠서 까지만 계산하고 자기를 더해주면 된다.
def solution(n):
    return n + sum([i for i in range(1, (n//2)+1) if n % i == 0])
  
  
n = 12
# n = 5
solution(n)