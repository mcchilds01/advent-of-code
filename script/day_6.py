def getForms1(forms_list: list) -> list:
    customsForms = []
    customsForm = []
    end = len(forms_list)
    for i in range(len(forms_list)):
        if forms_list[i] == '':
            customsForms.append(customsForm)
            customsForm = []
        else:
            customsForm += forms_list[i]
    customsForms.append(customsForm)
    return customsForms

def getForms2(forms_list: list) -> list:
    customsForms = []
    customsForm = []
    end = len(forms_list)
    for i in range(len(forms_list)):
        if forms_list[i] == '':
            customsForms.append(customsForm)
            customsForm = []
        else:
            customsForm.append(forms_list[i])
    customsForms.append(customsForm)
    return customsForms

def getCountsAny(forms_1: list) -> int:
    counts = []
    for i in range(len(forms)):
        counts.append(len(set(forms[i])))
    return sum(counts)

def getResponders(forms_2: list) -> list:
    responders = []
    for i in range(len(forms_2)):
        responders.append(len(forms_2[i]))
    return responders

def countsAll(forms_1: list, responders: list) -> int:
    formAllResponded = []
    allResponded = []
    for i in range(len(forms)):
        for j in range(len(forms[i])):
            if forms[i].count(forms[i][j]) == totalResponders[i]:
                formAllResponded += forms[i][j]
        if formAllResponded: 
            allResponded.append(len(set(formAllResponded)))
            formAllResponded = []
    return sum(allResponded)

with open("puzzle6_input.txt") as f:
    rows = [i.strip('\n') for i in f]

forms = getForms1(rows)
print(getCountsAny(forms))

totalResponders = getResponders(getForms2(rows))
print(countsAll(forms, totalResponders))