report_file = open("puzzle1_input.txt", "r")
expense_report = [int(i.strip()) for i in report_file.readlines()]
def get_solution_1(x):
    for i in x:
        for j in x:
            for k in x:
                if i + j + k == 2020:
                    ans = i*j*k  
    print(ans)

get_solution_1(expense_report)
