# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 푼 방법1
# def solution(x, n):
#     answer = []
#     for i in range(n+1):
#         answer.append(x*i)
#     return answer[1:]

# 푼 방법2
# def solution(x, n):
#     return [x*i for i in range(n+1)][1:]

# 다른 풀이 참고방법3
def solution(x, n):
    return [x*i for i in range(1, n+1)]


# x = 2
# n = 5
# x = 4
# n = 3
# x = -4
# n = 2
x = 0
n = 5

solution (x, n)