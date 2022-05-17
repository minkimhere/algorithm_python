# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.


# 참고 풀이 방법1
# base로 나눈 수의 나머지를 차례대로 하면 자연적으로 앞뒤 반전된 3진법으로 나오게 된다
# 몫과 나머지를 한 번에 구할 때는 divmod를 사용한다
# def solution(n):
#     answer = ''
#     while n > 0:
#         n, remainder = divmod(n, 3)
#         answer += str(remainder)
    # return int(answer,3)

# 참고 풀이 방법2
def solution(n):
  answer = ''
  while n > 0:
      answer += str(n%3)
      n//=3
  return int(answer, 3)

n = 45
# n = 1200
solution(n)