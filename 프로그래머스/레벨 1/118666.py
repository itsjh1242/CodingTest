
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"

'''
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)
'''



survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

score = {
        1 : 3,
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2,
        7 : 3
}

typeOfSurvey = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
scoreOfType = [0 for _ in typeOfSurvey]

for i, j in zip(survey, choices):
    flag = 0 if j < 4 else 1
    scoreOfType[typeOfSurvey.index(i[flag])] += score[j]
answer = ""
for _ in range(0, 7, 2):
    if scoreOfType[_] == scoreOfType[_ + 1]:
        answer += typeOfSurvey[_]
    else:
        answer += typeOfSurvey[_] if scoreOfType[_] > scoreOfType[_ + 1] else typeOfSurvey[_ + 1]
print(answer)

