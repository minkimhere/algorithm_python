# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.


# 푼 방법1
# def solution(x):
#     summation = sum(list(map(int,str(x))))
# #     return True if not x%summation else False

# def solution(x):
#     summation = sum(list(map(int,str(x))))
#     return x%summation == 0

# def solution(x):
#     return x%sum(list(map(int,str(x)))) == 0

solution = lambda x: x%sum(list(map(int,str(x)))) == 0




x = 10
x = 12
x = 11
x = 13
solution(x)