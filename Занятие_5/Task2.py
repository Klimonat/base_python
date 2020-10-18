with open("text_2.txt", encoding='utf-8') as file_obj:
    count_string = 0
    for line in file_obj:
        count_string += 1
        count_word = 0
        count_word = len(line.split())
        print("В строке {} - {} cлов".format(count_string, count_word))
    print("В файле {} строк".format(count_string))
