# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

# 푼 방법1
def solution(n):
    return ('수박'*n)[:n]
# def solution(n):
#     return ('수박'*(n-1))[:n]

# 다른 풀이 참고 방법2
  def solution(n):
    return '수박'*(n//2) + '수'*(n%2)

n = 3
# n = 4
solution(n)
