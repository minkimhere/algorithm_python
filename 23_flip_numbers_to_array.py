# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 푼 방법1
# def solution(n):
#     n = list(map(int, str(n)))
#     n.reverse()
    # return n

# 다른 방법2
# def solution(n):
#     return list(map(int, reversed(str(n))))

# 다른 방법3
# :: https://blog.wonkyunglee.io/3
# def solution(n):
#     return list(map(int, str(n)))[::-1]

# 다른 방법4
def solution(n):
    answer = []
    while n > 1:
        answer.append(int(n%10))
        n/=10
    return answer

n = 12345
solution(n)