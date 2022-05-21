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
#     return print('소수입니다.')

# 약수의 특성을 활용하면 연산 횟수를 반으로 줄일 수 있음.
# 예를들어 16의 약수 : 1 2 4 8 16 
# 4를 기준으로 1*16 2*8 식으로 대칭되어있음.
# 어차피 1로 나눴을 때 16이고 16으로 나눴을 때 1이고 둘다 나눠지니까 한 번만 검사해도 됨
# 따라서 4를 기준으로 왼쪽이 약수면 오른쪽도 확실히 약수임을 알 수 있음
# 그러면 16의 제곱근을 기준으로 작은 것만 검사하자

# def solution(nums):
#   print(int(nums**0.5 + 1))
#   for i in range(2, int(nums**0.5 + 1)):
#     print(i)
#     if nums % i == 0:
#       return print('소수가 아닙니다')
#   return print('소수입니다.')


# 2. array로 주어졌을 때 소수만 구하기
# nums = [1,5,7,8,9,11]
# nums가 배열일 때
# def solution(nums):
#   for num in nums:
#     if num < 2:
#       continue
#     for i in range(2, int(num**0.5 + 1)):
#       if num % i == 0:
#         break
#     print(num)


# 3. n1 n2가 주어졌을 때 n1, n2 사이에 있는 소수 구하기
# import sys

# a, b = map(int, sys.stdin.readline().split()) 

# for n in range(a, b+1):
#   if n < 2:
#     continue
#   for i in range(2, int(n**0.5) +1):
#     if n % i == 0:
#       break
#   else: 
#     print(n)


# 3 다른 풀이
# 에라토스테네스의 체
# https://www.acmicpc.net/source/28320052
# https://velog.io/@gillog/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
# def solution(m, n):
#   sieve = [True] * (n+1)
#   for i in range(2, int(n**0.5)+1):
#       print('아이', i)
#       # if sieve[i]:
#       for j in range(i*2, n+1, i): # 자기 자신은 소수니까 제외하고 만약 3이라면 3은 이미 소수니까 제외하고 6부터 지울건데 3의 배수로 지울거니까 3번째 파라미터로 i(3)씩 배수로 해준다는 뜻
#         print('제이', j)
#         sieve[j] = False
  # for i in range(m, n):
    # if i > 1:
      # if sieve[i]:
        # print(i)


# 백준 제출용
import sys

m, n = map(int, sys.stdin.readline().split())

# 체
sieve = [True] * (n+1) 

for i in range(2, int(n**0.5)+1): # 1 2 4 8 16 이라면, (1,16) (2,8) 짝 지어져서 어차피 1,2만 검사하면 뒤도 같은 효과라서 앞 부분만 검사해도 됨
    for j in range(i*2, n+1, i): # 에라토스테네스의 체 가장 작은 수(지우면서 맨 처음 남아있는 작은 수는 어차피 소수임) 제외 자기의 배수로 지우기
        sieve[j] = False
for i in range(m, n+1):
    if i > 1:
        if sieve[i]:
            print(i)
        


# nums = 99
# nums = [1,5,7,8,9,11]
# solution(nums)
# solution(n1, n2)

# m = 3
# n = 16
# solution(m, n)