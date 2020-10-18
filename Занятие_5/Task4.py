with open("text_4.txt", 'r', encoding='utf-8') as input_file:
    with open("text_4_final.txt", 'a', encoding='utf-8') as final_file:
        num_str = 0
        for line in input_file:
            num_str += 1
            if num_str == 1:
                name = 'Один'
            elif num_str == 2:
                name = 'Два'
            elif num_str == 3:
                name = 'Три'
            else:
                name = 'Четыре'
            number = line.split()[2]
            print(name + ' - ' + number, file=final_file)