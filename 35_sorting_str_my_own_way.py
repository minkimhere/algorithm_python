# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.


# 참고 자료
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda#:~:text=To%20define%20lambda%2C%20you%20specify,as%20the%20third%20argument(Optional.

# sorted(iterable, key=key, reverse=reverse)
# 주어진 입력 배열:people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

# line: 다음과 같이 목록을 people_sort = sorted(people, key = lambda x: (-x[0], x[1]))제공합니다 .people_sort[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

# 이 경우 key=lambda x: (-x[0], x[1])기본적으로 각 인스턴스의 첫 번째 요소 값을 기준으로 배열 sorted을 먼저 정렬( 빼기 기호가 암시하는 대로 내림차순 ) 한 다음 동일한 하위 그룹 내에서 각 인스턴스의 두 번째 요소를 기준 으로 정렬하도록 지시합니다. 인스턴스(기본 옵션이므로 오름차순).

# strings의 sun, bed, car의 n번째 문자를 기준으로 먼저 sort.(x[n])
# n이 1이라면, u,e,a를 기준으로 a,e,u 순서대로 먼저 sort됨.
# 그 다음으로 abcd abce 같은 경우를 순서대로 하기 위해서 두번째로 sun, bed, car 자체도
# sort해주기 위해서 x를 sort함.


# 참고 방법1
# def solution(strings, n):
#     return sorted(strings, key = lambda x:(x[n], x))

# solution = lambda strings,n : sorted(strings, key = lambda x:(x[n], x))

# best
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x:(x[n]))
  
# 방법2
# def solution(strings, n):
#     answer = []
#     for i in range(len(strings)):
#         strings[i] = strings[i][n] + strings[i]
#     strings.sort()
#     for string in strings:
#         answer.append(string[1:])
#     return answer

# 방법3
# def solution(strings, n):
#     answer = []
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     strings.sort()
#     for a in alphabet:
#         for string in strings:
#             if string[n] == a:
#                 answer.append(string)
#     return answer


strings = ["sun", "bed", "car"]
n = 1
# strings = ["abce", "abcd", "cdx"] 
# n = 2
solution(strings, n)