# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


# 푼 방법1
# def solution(s):
#     answer = ''
#     s = s.split(' ')
#     for i in range(len(s)):
#         word = list(s[i])
#         for j in range(len(word)):
#             if j % 2 == 0:
#                 word[j] = word[j].upper()
#             else:
#                 word[j] = word[j].lower()
#         word = ''.join(word)
#         answer += word + ' '
#     return answer[:-1]

# 푼 방법2
# def solution(s):
#   answer = ''
#   s = s.split(' ')
#   for word in s:
#       x = ''
#       for i in range(len(word)):
#           if i % 2 == 0:
#               x += word[i].upper()
#           else:
#               x += word[i].lower()
#       answer += x + ' '
#   return answer[:-1]

# 다른 풀이 참고 방법3
# def solution(s):
#     answer = ''
#     s = s.split(' ')
#     for word in s:
#         x = ''
#         for count, ele in list(enumerate(word)):
#             if count % 2 == 0:
#                 x += ele.upper()
#             else:
#                 x += ele.lower()
#         answer += x + ' '
#     return answer[:-1]

  
# 다른 풀이 참고 방법4
def solution(s):
    return ' '.join([ ''.join([ele.upper() if count % 2 == 0 else ele.lower() for count, ele in enumerate(word)]) for word in s.split(" ")])


s = "try hello world"
solution(s)
