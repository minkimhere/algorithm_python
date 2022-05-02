# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 푼 방법1
# def solution(absolutes, signs):
#     for i, n in enumerate(signs):
#         if signs[i] == False:
#             absolutes[i] = absolutes[i] * -1
#     return sum(absolutes)


# 다른 풀이 참고 방법2
# def solution(absolutes, signs):
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             absolutes[i] = absolutes[i] * -1
#     return sum(absolutes)
    

# 다른 풀이 참고 방법3
# def solution(absolutes, signs):
#     answer = [];
#     for absolutes, signs in zip(absolutes, signs):   
#         if signs: answer.append(absolutes)
#         else : answer.append(-absolutes)
#     return sum(answer)

# 다른 풀이 참고 방법4

# a = [1]
# b = [2]
# * zip(a, b) = (1, 2)
# zip은 합칠 때 쓴다.

# 한 줄에 for문을 출력할 때는 앞에 출력을 원하는 것, 뒤에 for문을 쓰면 된다.

# 과정1
# def solution(absolutes, signs):
#     return print(absolutes for absolutes, signs in zip(absolutes, signs))
# 과정2
# def solution(absolutes, signs):
#     return print(list(absolutes for absolutes, signs in zip(absolutes, signs)))
# 과정3
# def solution(absolutes, signs):
#     return print(list(absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs)))
# 완성
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
  
  
# absolutes = [4,7,12]
# signs = [True, False, True]
absolutes = [1,2,3]
signs= [False, False, True]

solution(absolutes, signs)