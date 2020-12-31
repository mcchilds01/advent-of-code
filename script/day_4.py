def getPassports(data):
    passport_data = []
    passports = []
    for i in range(len(data)):
        if data[i] == '':
            passports.append(passport_data)
            passport_data = []
            if '' not in rows[i+1:len(data)]:
                passport_item = [x.strip() for x in data[i].strip(' ')]
                passport_data += passport_item
                passports.append(passport_data)
        else: 
            passport_item = [x.strip() for x in data[i].split(' ')]
            passport_data += passport_item
    return passports

def checkPpt1(data, test):
    return all(x in str(data) for x in test)

def checkPpt2(passport):
    valid_fields = 0
    eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if int(passport['byr']) in range(1920, 2003):
        valid_fields += 1
    if int(passport['iyr']) in range(2010, 2021):
        valid_fields += 1
    if int(passport['eyr']) in range(2020, 2031):
        valid_fields += 1
    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) in range(150, 194):
            valid_fields += 1
    if passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) in range(59, 77):
            valid_fields += 1
    if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
        valid_fields += 1
    if passport['ecl'] in eyeColors:
        valid_fields += 1
    if len(passport['pid']) == 9:
        valid_fields += 1
    
    if valid_fields == 7:
        return True
    else: return False

def makeDict(passports: list) -> dict:
    passport_dict = {}
    for field in passports:
        field_label, field_value = field.split(':')
        passport_dict[field_label] = field_value
    return passport_dict

with open('puzzle4_input.txt') as p:
    rows = [row.strip() for row in p.readlines()]

valid_passports = []
validCount = 0
test = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validityTest1 = getPassports(rows)
for i in validityTest1:
    if checkPpt1(i, test):
        valid_passports.append(i)
        validCount += 1
print('Part I: ' + str(validCount))

passport_dicts = []
for i in range(len(valid_passports)):
    passport_dicts.append(makeDict(valid_passports[i]))

totalCount = len(passport_dicts)
for i in range(len(passport_dicts)):
    if checkPpt2(passport_dicts[i]) == False:
        totalCount -= 1
print('Part II: ' + str(totalCount))

