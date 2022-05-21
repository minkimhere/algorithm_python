# 소수 구하기 연습문제
# 1. n이 주어졌을 때 n이 소수인지 판별
# 2. array로 주어졌을 때 소수만 구하기
# 3. n1 n2가 주어졌을 때 n1, n2 사이에 있는 소수 구하기
# -> 백준 1929번 M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# https://www.acmicpc.net/problem/1929


# https://seongonion.tistory.com/43
# 소수는 영어로 Prime Number라고 부르며 1과 자기자신 외에는 어떠한 수로도 나누어 떨어지지 않는 수를 말한다. 

# 특정 수 N이 소수인지 아닌지 구하는 법은 바로 이 특징을 활용하여 2부터 N-1 까지의 수로 해당 수를 나눠보고, 이 과정에서 어떠한 수에 의해 나누어 떨어지는지 확인하는 것이다.

#   나누어떨어지지 않는다면 해당 수는 소수인 것이고, 도중에 다른 수에 의해 나누어 떨어진다면 그 수는 소수가 아닐 것이다.

# 1. n이 주어졌을 때 n이 소수인지 판별
# nums = 18 일 때
# def solution(nums):
#     for i in range(2, nums):
#      if nums % i == 0:
#        return print('소수가 아닙니다.')
#      else:
#        return print('소수입니다.')

# 약수의 특성을 활용하면 연산 횟수를 반으로 줄일 수 있음.
# 예를들어 16의 약수 : 1 2 4 8 16 
# 4를 기준으로 1*16 2*8 식으로 대칭되어있음.
# 어차피 1로 나눴을 때 16이고 16으로 나눴을 때 1이고 둘다 나눠지니까 한 번만 검사해도 됨
# 따라서 4를 기준으로 왼쪽이 약수면 오른쪽도 확실히 약수임을 알 수 있음
# 그러면 16의 제곱근을 기준으로 작은 것만 검사하자

# def solution(nums):
#   for i in range(2, int(nums**0.5 + 1)):
#     if nums % i == 0:
#       return print('소수가 아닙니다')
#     else:
#       return print('소수입니다.')


# 2. array로 주어졌을 때 소수만 구하기
# nums = [1,5,7,8,9,11]
# nums가 배열일 때
# def solution(nums):
#   for num in nums:
#     if num < 2:
#       continue
#     for i in range(2, int(num**0.5 + 1)):
#       if num % i != 0:
#         print(num)

# 3. n1 n2가 주어졌을 때 n1, n2 사이에 있는 소수 구하기
# import sys

# n1, n2 = map(int, sys.stdin.readline().split())

def solution(n1, n2):
  for n in range(n1, n2+1):
    if n == 1:
      continue
    for i in range(2, int(n**0.5) +1):
      if n % i == 0:
        break
    else: 
      print(n)

      
# nums = 18
# nums = [1,5,7,8,9,11]
n1 = 1
n2 = 16
solution(n1, n2)