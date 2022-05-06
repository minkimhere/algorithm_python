# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 푼 방법1
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         sum = []
#         for j in range(len(arr1[0])):
#             sum.append(arr1[i][j] + arr2[i][j])
#         answer.append(sum)  
#     print(answer)

# 다른 풀이 참고 방법2
# 과정1
# def solution(A, B):
#     answer = []
#     for a, b in zip(A,B):
#         sum = [a, b]    
#         answer.append(sum)
#     print(answer)

# 과정1과 2는 answer 값이 동일
# 과정2
# def solution(A, B):
#     answer = [[a, b] for a, b in zip(A,B)]
#     print(answer)

# 과정3
def solution(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    print(answer)



arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# arr1 = [[1],[2]]
# arr2 = [[3],[4]]

solution(arr1, arr2)