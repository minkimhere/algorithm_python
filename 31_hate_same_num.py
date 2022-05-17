# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


# 참고 방법1
# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if i == 0:
#             answer.append(arr[i])
#         elif arr[i] != arr[i-1]:
#             answer.append(arr[i])
#     return answer

# best
# 방법2
def solution(arr):
    answer = []
    answer.append(arr[0])
    for n in arr:
        if n != answer[-1]:
            answer.append(n)                
    return answer

# 방법3
# [-1]로 하면 answer은 처음에 아예 빈 배열이기 때문에 이 안에 거를 꺼낼 때 오류남. 
# 그래서 아예 [-1:]로 하면 []로 비교할 수 있음
# def solution(arr):
#     answer = []
#     for n in arr:
#         if answer[-1:] != [n]:
#             answer.append(n)
#     return answer

# 방법4
# def solution(arr):
#     return [n for i,n in enumerate(arr) if i==0 or arr[i-1]!=arr[i] ]

# arr맨 뒤값과 맨 앞값이 같으면 arr의 맨 앞값 추가해주고 쭉 비교하는 거라서 이게 더 빠르다.
# 만약 추가를 안해주면 [1,1,3,1] 같은 상황에서 맨뒤, 맨 앞 같으니까 1추가 안되고, 맨앞 그 바로 뒤 같으니까 1추가 안돼서 1이 누락된다.
# (i==0)을 앞쪽에 두면 매번 검사해야하므로 조금 느려짐
# def solution(arr):
#     return [n for i,n in enumerate(arr) if arr[i-1]!=arr[i] or i==0]

arr = [1,1,3,3,0,1,1]
# arr = [4,4,4,3,3]
solution(arr)

