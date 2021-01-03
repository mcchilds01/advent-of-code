def getForms1(forms_list: list) -> list:
    customsForms = []
    customsForm = []
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
    for i in range(len(forms_list)):
        if forms_list[i] == '':
            customsForms.append(customsForm)
            customsForm = []
        else:
            customsForm.append(forms_list[i])
    customsForms.append(customsForm)
    return customsForms

def getCountsAny(forms_1: list) -> int:
    counts = [len(set(forms[i])) for i in range(len(forms))]
    return sum(counts)

def getResponders(rows: list) -> list:
    forms_2 = getForms2(rows)
    responders = [len(forms_2[i]) for i in range(len(forms_2))]
    return responders

def countsAll(forms_1: list, responders: list) -> int:
    allResponded = []
    for i in range(len(forms)):
        formAllResponded = [forms[i][j] for j in range(len(forms[i])) 
            if forms[i].count(forms[i][j]) == totalResponders[i]]
        if formAllResponded: 
            allResponded.append(len(set(formAllResponded)))
            formAllResponded = []
    return sum(allResponded)

with open("puzzle6_input.txt") as f:
    rows = [i.strip('\n') for i in f]

forms = getForms1(rows)
print('Part I:', getCountsAny(forms))

totalResponders = getResponders(rows)
print('Part II:', countsAll(forms, totalResponders))
