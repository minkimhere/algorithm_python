# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# s = "abcde"
s = "qwer"
# s = "avcxvxcv"

def solution(s):
  half = len(s)//2
  result = s[half]  if len(s) % 2 else s[half-1 : half+1]
  print(result)

solution(s)