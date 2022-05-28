# 프로그래머스 약수의 개수와 덧셈 https://programmers.co.kr/learn/courses/30/lessons/77884

# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	43
# 24	27	52


# 방법1
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        count = 0
        for j in range(1, n+1):
            if n % j == 0:
                count += 1
        
        if count % 2 == 0:
            answer += n
        else:
            answer -= n
    
    return answer


left = 13
right = 17
solution(left, right)