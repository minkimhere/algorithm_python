# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# a, b = map(int, input().strip().split(' '))

# 푼 방법1
a = 5;
b = 3;

for _ in range(b):
  print(a * "*")

# 푼 방법2
# 반복하는 메소드
# import itertools

# for i in itertools.repeat("*", b):
#   print(i * a )

# 다른 풀이
# answer = ('*' * a + '\n') * b
# print(answer)