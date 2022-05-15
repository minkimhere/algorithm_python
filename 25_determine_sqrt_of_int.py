# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.


# 방법1
# def solution(n):
#     return (n**0.5+1)**2 if n == int(n**0.5)**2  else -1

# 방법2
# def solution(n):
#     return ((n == int(n**0.5)**2) and (n**0.5+1)**2) or -1

# 방법3
# and가 or보다 우선순위 높으므로 괄호 안해도 됨
# def solution(n):
#     return ((n**0.5)%1==0 and (n**0.5+1)**2) or -1
# def solution(n):
#     return (n**0.5)%1==0 and (n**0.5+1)**2 or -1

# 방법4
def solution(n):
    return (n**0.5+1)**2 if (n**0.5)%1==0  else -1


n = 121
# n = 2
solution(n)