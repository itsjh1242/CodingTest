# def solution(survey, choices):
#     result = {
#         "A" : 0, 
#         "C" : 0,
#         "F" : 0,
#         "J" : 0,
#         "M" : 0,
#         "N" : 0,
#         "R" : 0,
#         "T" : 0
#     }

    # score = {
    #     1 : 3,
    #     2 : 2,
    #     3 : 1,
    #     4 : 0,
    #     5 : 1,
    #     6 : 2,
    #     7 : 3
    # }


#     choicesOfSurvey = {}
#     for s, c in zip(survey, choices):
#         choicesOfSurvey[s] = c

#     flag = 0

#     for k, v in choicesOfSurvey.items():
#         if v == 4: continue
#         flag = 0 if v < 4 else 1
#         result[k[flag]] += score[v]

#     def big(a, b):
#         return a if a < b else b

#     mbti = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
#     answer = ""
#     for _ in mbti:
#         if result[_[0]] == result[_[1]]:
#             answer += big(_[0], _[1])
#         elif result[_[0]] > result[_[1]]:
#             answer += _[0] 
#         else:
#             answer += _[1]

#     return answer
'''
point = {}
for s, c in zip(survey, choice):
    flag = 0 if c < 4 else 1
    if s[flag] in point:
        point[s[flag]] += score[c]
    else:
        point[s[flag]] = score[c]
'''

survey = ["AN", "CF", "MJ", "RT", "NA"]
choice = [5, 3, 2, 7, 5]
score = {
        1 : 3,
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2,
        7 : 3
    }
point = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
for s, c in zip(survey, choice):
    flag = 0 if c < 4 else 1
    point[s[flag]] += score[c]
answer = ""
indicatorA = {}
for i, k, v in enumerate(point.items()):
    print(i, k, v)
    
