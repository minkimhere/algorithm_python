# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

# 방법1
# https://www.geeksforgeeks.org/python-dictionary-items-method/
# dictionart items() 사용
# keys, values, items는 리스트 형태로 (key, value) 튜플을 받을 수 있는데, 신기하게도 O(1)로 작동합니다. for문에서 잘 활용하시면 불필요한 연산을 많이 줄일 수 있습니다.
# Dictionary with three items 
# Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

#-> items() 사용시 다음과 같이 쓸 수 있음
# Dictionary items:
# dict_items([('A', 'Geeks'), ('B', 4), ('C', 'Geeks')])

# def solution(s):
#     num = {'zero' :0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
#     for n in num.items():
#         s = s.replace(n[0], str(n[1]))
        
#     return int(s)

# def solution(s):
#     num = {'zero' :'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
#     for key, value in num.items():
#         s = s.replace(key, value)
        
#     return int(s)

# 방법2 enumerate사용
def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i, n in enumerate(num):
        s = s.replace(n, str(i))
    
    return int(s)


s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"
solution(s)