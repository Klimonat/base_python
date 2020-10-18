with open("text_6.txt", encoding='utf-8') as file_obj:
    subject = []
    dictionary = {}
    for line in file_obj:
        subject = line.split()
        name = ''
        quantity = 0
        name = subject[0][:-1]
        for count in subject[1:]:
            number = count.find('(')
            if number != -1:
                quantity += int(count[:number])
        dictionary[name] = quantity
print(dictionary)
