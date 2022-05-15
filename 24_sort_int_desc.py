# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.


# 푼 방법1
# def solution(n):
#     answer = []
#     while n>1:
#         answer.append(int(n%10))
#         n/=10
#     answer.sort(reverse=True)
#     answer = list(map(str, answer))
#     return int(''.join(answer))

# 다른 방법2
# def solution(n):
#     n = list(str(n))
#     n.sort(reverse=True)
#     return int(''.join(n))

# 다른 방법3
# def solution(n):
#     return int(''.join(sorted(list(str(n)), reverse=True)))
# sorted 하면 배열로 sort해서 나옴
def solution(n):
    return int(''.join(sorted((str(n)), reverse=True)))


n = 118372
solution(n)