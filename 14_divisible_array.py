# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 푼 방법1
# def solution(arr, divisor):
#     answer = []
#     for n in sorted(arr):
#         if not n % divisor:
#             answer.append(n)
#     if len(answer) == 0:
#         return [-1]
#     else:
#         return answer

# 풀이 참고 방법2
# python은 or 앞이 참일 경우 해당 값 까지만, 거짓일 경우 뒤에 것까지 호출
# def solution(arr, divisor):
#     return sorted([n for n in arr if not n%divisor]) or [-1]

# 풀이 참고 방법3
def solution(arr, divisor): 
    return sorted(list(filter(lambda x: x%divisor == 0 ,arr))) or [-1]
    

arr = [5, 9, 7, 10]
divisor = 5
# arr = [3,2,6]	
# divisor= 10
solution(arr, divisor)