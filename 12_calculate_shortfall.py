# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 푼 방법1
# def solution(price, money, count):
#     sum = 0;
#     for n in range(1, count+1):
#         sum += price * n
#     return (0 if money>=sum else sum - money)

# 다른 풀이 참고 방법2
# 등차수열 공식을 이용한 방법
# (1+2+3+4) * 3 = 30 등차수열 * price
# 3*1 + 3*2 + 3*3 + 3*4 = 30 price * 첫번째 + price * 두번째
# 등차수열을 이용했을 때와 값이 같다.
# 금액이 부족하지 않을 때는 오른쪽 식이 -가 되므로, max를 사용해서 0이 더 클 때로 구해줌
def solution(price, money, count):
    return max(0, (count*(count+1)//2) * price - money)

price = 3
money = 20
count = 4

solution(price, money, count)