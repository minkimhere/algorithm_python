# 프로그래머스 시저암호 https://programmers.co.kr/learn/courses/30/lessons/12926
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

# 방법1
def solution(s, n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for char in s:
        if char in lower:
            print(char)
            i = lower.find(char) + n
            answer += lower[i%26]
        elif char in upper:
            print(char)
            i = upper.find(char) + n
            answer += upper[i%26]
        else:
            answer += ' '
    return answer


# 방법2
# import string을 한 뒤 string.ascii_lowercase)를 사용하면 'abcd...z'를 만들어줌
# string.find()를 하면 문자열의 인덱스를 알려줌
import string
 
def solution(s, n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    answer = ''

    for char in s:
        if char == ' ':
            answer += ' '
        elif char.islower():
            i = lower.find(char) + n
            answer += lower[i % 26]
        else:
            i = upper.find(char) + n
            answer += upper[i % 26]
    return answer


# 방법3
# https://ourjes.tistory.com/59
# 아스키코드를 활용한 방법
def solution(s, n):
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '
        elif ord(char) >= 65 and ord(char) <= 90:
            askii = ord(char) + n
            if askii > 90:
                answer += chr(askii - 26) # 90(아스키코드 Z)넘기면 다시 맨 앞으로 땡겨와야함
            else:
                answer += chr(askii)
        else:
            askii = ord(char) + n
            if askii > 122:
                answer += chr(askii - 26) # 122(아스키코드 Z)넘기면 다시 맨 앞으로 땡겨와야함
            else:
                answer += chr(askii)
    return answer

# 방법4
# # https://s2cherryy.tistory.com/24
# 1) 대문자일때, 소문자일때 구분한다.
# 2) 대문자일때 -> 몇번째 알파벳인지를 확인한다. : ord(s[i]) - ord('A)
# 3) 알아낸 알파벳 번호 + 밀기 번호
# 4) %26으로 z or Z를 벗어난 알파벳을 잡는다.
# 5) 실제 아스키코드 번호를 구하기 위해 'A'의 아스키코드를 더해준다.
  
# 아스키코드를 활용한 방법2
def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += ' '
        elif char.isupper():
            answer += chr(( ord(char) - ord('A') + n)%26 + ord('A')) # 그 숫자의 위치에서 n 만큼 더하기 위해서 숫자를 아스키코드로 바꿔준다음에 숫자를 더할 수 있도록 한다.
          # A를 빼준다. 예를들어서 원래 A가 있고 이것을 아스키코드로 바꾸면 65가 됨. 그런데 이건 숫자(n)를 더하기 위해서 아스키코드로 바꿔놓은 것이기 때문에 원래 문자였던 ABCD 순서대로 하고 A의 순서인 0을 구하기 위해서 아스키코드('A')를 빼주면 그냥 문자의 순서(index) 번호를 알 수 있다. 한 마디로 s의 각각 문자 + n 을 더한 것의 index 넘버를 알아냈다고 볼 수 있다.
        else:
            answer += chr(( ord(char) - ord('a') + n)%26 + ord('a'))
    return answer
 


s = "AB"	
n = 1
# s = "z"	
# n = 1
# s = "a B z"
# n = 4
def solution(s, n)