# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 푼 방법1
# def solution(n):
#     return sum(list(map(int, str(n))))

# 다른 사람 풀이 참고 방법2
def solution(n):
    return n if n < 10 else n % 10 + solution(n//10)

n = 123
# n = 987
solution(n)