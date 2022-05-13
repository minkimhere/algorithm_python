# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 방법1
# isdigit() https://blockdmask.tistory.com/556
# isdigit() 시간복잡도 https://trey-de.tistory.com/7 
# isdigit -> O(n)
# def solution(s):
#     return s.isdigit() and len(s) == 4 or len(s) == 6


# 방법2
# 얼핏 보면 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용하는 것이 유리하다. 튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 여부이다. 즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다. 따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 주저하지 말고 튜플을 사용해야 한다. 
# 튜플 https://wikidocs.net/15
# def solution(s):
#     return s.isdigit() and len(s) in [4,6]
# def solution(s):
#     return s.isdigit() and len(s) in (4,6)


# 방법3
# 파이썬 내장함수 시간 복잡도 https://velog.io/@ggyungjun0913/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84
# len() -> O(1)
# str() -> O(logn)
# list, tuple -> O(n)
# def solution(s):
#     if len(s) in (4,6):
#         try:
#             return (bool(int(s)))
#         except:
#             return False
#     else:
#         return False

# 방법4
def solution(s):
    try: int(s)
    except: return False
    return len(s) in (4,6)


s= "a234"
s = "1234"
solution(s)