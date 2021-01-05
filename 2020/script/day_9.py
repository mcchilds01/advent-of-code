with open('puzzle9_input.txt') as f:
    numbers = [int(i) for i in f]

def getWeakness(numbers_list: list, preamble_length: int) -> int:
    sorted_preamble = []
    sums = []
    for i in range(len(numbers_list)):
        if i < preamble_length:
            continue
        else: 
            sorted_preamble = sorted(numbers_list[i-preamble_length:i])
            sums = [sorted_preamble[j]+sorted_preamble[k] for j in range(len(sorted_preamble)) for k in 
                range(len(sorted_preamble)) if sorted_preamble[j]+sorted_preamble[k] == numbers_list[i]]
            if sums == []:
                return numbers_list[i]
            sums = []

print("Part I:", getWeakness(numbers, 25))

def getWeakness2(numbers_list: int, number: int) -> int:
    sums = 0
    for i in range(len(numbers_list)):
        for j in range(i, len(numbers_list)-1):
            sums += numbers_list[j]
            if sums == number:
                return min(numbers_list[i:j+1]) + max(numbers_list[i:j+1])
        sums = 0

print("Part II:", getWeakness2(numbers, 25918798))
