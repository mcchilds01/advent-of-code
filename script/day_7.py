with open('puzzle7_input.txt') as f:
    rules = [i.strip() for i in f]

newRules = [i.split('contain') for i in rules]

def getPossibleBagsInside(rules_list, terms_list):
    answers = [j[0].replace('bags','').strip() for i in range(len(terms_list)) 
        for j in rules_list for x in range(len(j)) if terms_list[i] in j[x][2:-4]]
    return answers

def getTotalInside(rules_list: list, possible_bags: list) -> int:
    totals = []
    for i in range(len(rules_list)):
        options = getPossibleBagsInside(rules_list, possible_bags)
        totals += set(options)
        possible_bags = options
        if options == []:
            break
    return len(set(totals))

print("Part I:", getTotalInside(newRules, ["shiny gold"]))

def getPossibleBagsOutside(rules_list, terms_list):
    bagRules = {}
    for i in range(len(rules_list)):
        container = rules_list[i][0].replace('bags','').strip()
        contained = rules_list[i][1].replace('.','').replace('bags','').replace('bag','').strip().split(',')
        bagRules[container] = contained
    return bagRules

def getTotalOutside(rules_dict: dict, bag_type: str) -> int:
    totals = 0
    if rules_dict[bag_type] == ['no other']:
        return 0 
    else: 
        interimTotal = sum(int(innerBag[:2]) + int(innerBag[:2])*getTotalOutside(bagRules, innerBag[2:].strip()) for innerBag in bagRules[bag_type])
        totals += interimTotal
    return(totals)

bagRules = getPossibleBagsOutside(newRules, "shiny gold")

print('Part II:', getTotalOutside(bagRules, 'shiny gold'))