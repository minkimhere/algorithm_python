# 프로그래머스 최대공약수와 최소공배수 https://programmers.co.kr/learn/courses/30/lessons/12940

# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.


# 방법1
# https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level1-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
# https://kworld.tistory.com/120
#유클리드 호제법 공식
# 임의의 두 자연수 a, b가 주어졌을 때, 둘 중 큰 값을 b라고 가정한다.
# b를 a로 나눈 나머지를 n이라고 한다면(b % a = n), n(나머지)이 0일때, a가 최대 공약수(GCD)이다.
# 만약 n이 0이 아니라면, a에 b값을 다시 넣고 n(나머지)를 b에 대입한 후 n이 0이 될 때까지 a % b를 반복한다.
# 유클리드 호제법 사용
def solution(n, m):
    a, b = min(n,m), max(n,m)
    while b % a: # 나머지가 0이 아닐 때만 계속 반복해서 대입 시킴
        remainder = b % a
        b = a
        a = remainder
    
    return [a, n*m/a]


n = 3
m = 12
solution(n, m)