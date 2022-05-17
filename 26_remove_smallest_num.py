# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.


# 푼 방법1
# def solution(arr):
#     if len(arr) in (0, 1):
#         return [-1]
#     else:
#         num = min(arr)
#         answer = arr.index(num)
#         arr.pop(answer)
#         return arr
# def solution(arr):
#     if len(arr) == 0 or len(arr) == 1:
#         return [-1]
#     else:
#         num = min(arr)
#         answer = arr.index(num)
#         arr.pop(answer)
#         return arr
# def solution(arr):
#     if len(arr) == 0 or len(arr) == 1:
#         return [-1]
#     else:
#         arr.pop(arr.index(min(arr)))
#         return arr


# 다른 풀이 참고 방법2
# def solution(arr):
#     if len(arr) in (0,1):
#         return [-1]
#     else:
#         arr.remove(min(arr))
#         return arr

# 방법3
def solution(arr):
    if len(arr) == 0 or len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

arr = [4,3,2,1]
# arr = [10]
solution(arr)