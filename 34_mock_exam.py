# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.


# 참고 방법1
# def solution(answers):
#     user1 = [1,2,3,4,5]
#     user2 = [2,1,2,3,2,4,2,5]
#     user3 = [3,3,1,1,2,2,4,4,5,5]
#     count1, count2, count3 = 0, 0, 0
    
#     for i in range(len(answers)):
#         i1 = i % 5
#         i2 = i % 8
#         i3 = i % 10
#         if user1[i1] == answers[i]:
#             count1 += 1
#         if user2[i2] == answers[i]:
#             count2 += 1
#         if user3[i3] == answers[i]:
#             count3 += 1
    
#     maxN = max(count1, count2, count3)
#     answer = []

#     if maxN == count1:
#         answer.append(1)
#     if maxN == count2:
#         answer.append(2)
#     if maxN == count3:
#         answer.append(3)
#     return sorted(answer)

# def solution(answers):
#     user1 = [1,2,3,4,5]
#     user2 = [2,1,2,3,2,4,2,5]
#     user3 = [3,3,1,1,2,2,4,4,5,5]
#     score1, score2, score3 = 0, 0, 0
    
#     for i in range(len(answers)):
#         i1 = i%len(user1)
#         i2 = i%len(user2)
#         i3 = i%len(user3)
#         if user1[i1] == answers[i]:
#             score1 += 1
#         if user2[i2] == answers[i]:
#             score2 += 1
#         if user3[i3] == answers[i]:
#             score3 += 1
    
#     answer = []
#     maxN = max(score1, score2, score3)
#     if maxN == score1:
#         answer.append(1)
#     if maxN == score2:
#         answer.append(2)
#     if maxN == score3:
#         answer.append(3)
#     return answer


# 방법2
def solution(answers):
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    answer = []
    
    for i, n in enumerate(answers):
        if n == user1[i%5]:
            score[0] += 1
        if n == user2[i%8]:
            score[1] += 1
        if n == user3[i%10]:
            score[2] += 1
    
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
            
    return answer

# def solution(answers):
#   user1 = [1,2,3,4,5]
#   user2 = [2,1,2,3,2,4,2,5]
#   user3 = [3,3,1,1,2,2,4,4,5,5]
#   score = [0, 0, 0]
#   answer = []
  
#   for i, n in enumerate(answers):
#       if n == user1[i%len(user1)]:
#           score[0] += 1
#       if n == user2[i%len(user2)]:
#           score[1] += 1
#       if n == user3[i%len(user3)]:
#           score[2] += 1
  
#   for i, s in enumerate(score):
#       if s == max(score):
#           answer.append(i+1)
          
#   return answer



answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]

solution(answers)