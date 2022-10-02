# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"

'''
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)
'''

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

#  expected result = TCMA

result = {
    "A" : 0, 
    "C" : 0,
    "F" : 0,
    "J" : 0,
    "M" : 0,
    "N" : 0,
    "R" : 0,
    "T" : 0
}

score = {
    1 : 3,
    2 : 2,
    3 : 1,
    4 : 0,
    5 : 1,
    6 : 2,
    7 : 3
}


choicesOfSurvey = {}
for s, c in zip(survey, choices):
    choicesOfSurvey[s] = c

flag = 0

for k, v in choicesOfSurvey.items():
    if v == 4: continue
    flag = 0 if v < 4 else 1
    result[k[flag]] += score[v]

def big(a, b):
    return a if a < b else b

mbti = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
answer = ""
for _ in mbti:
    if result[_[0]] == result[_[1]]:
        answer += big(_[0], _[1])
    elif result[_[0]] > result[_[1]]:
        answer += _[0] 
    else:
        answer += _[1]

print(answer)

