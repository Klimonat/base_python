with open("text_3.txt", encoding='utf-8') as file_obj:
    staff = 0
    sum_salary = 0
    employee_min_20 = ''
    for line in file_obj:
        salary = 0
        name = ''
        staff += 1
        name = line.split()[0]
        salary = float(line.split()[1])
        if float(salary) < 20000:
            employee_min_20 += name + ' '
        sum_salary += salary
    print("Средняя зарплата: ", sum_salary / staff)
    print("Сотрудники, оклад которых менее 20000:", employee_min_20)
