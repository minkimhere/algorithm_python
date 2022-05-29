# 프로그래머스 약수의 개수와 덧셈 https://programmers.co.kr/learn/courses/30/lessons/77884

# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	43
# 24	27	52


# 방법1
# def solution(left, right):
#     answer = 0
#     for n in range(left, right+1):
#         count = 0
#         for j in range(1, n+1):
#             if n % j == 0:
#                 count += 1
        
#         if count % 2 == 0:
#             answer += n
#         else:
#             answer -= n
    
#     return answer


# 방법2
# https://programmers.co.kr/learn/courses/30/lessons/77884/solution_groups?language=python3
# 제곱수의 약수는 홀수개이다. -> 홀수개의 약수를 가진 수는 제곱이 될 수 있다. -> 제곱근으로 만든 후 비교해준다. -> 그래서 int(n**0.5)와 n**0.5를 비교해서 똑같으면 그게 약수를 홀수개로 가진 숫자이다. 왜냐하면 약수를 짝수개로 가진 숫자는 3.33333 같은 수로 나와서 int를 씌워서 비교해도 다를 것이지만, 약수를 홀수개로 가진 숫자는 4.0 같은 수로 나와서 제곱이 될 수 있으므로 int를 씌워주지 않아도 같다.
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if int(n**0.5) ==  n**0.5:
            answer -= n
        else:
            answer += n
    return answer

left = 13
right = 17
solution(left, right)