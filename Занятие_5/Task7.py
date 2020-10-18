import json

with open("text_7.txt", 'r', encoding='utf-8') as input_file:
    dictionary_prof = {}
    dictionary = {}
    name = ''
    profit = 0
    average_profit = 0
    count = 0
    for line in input_file:
        subject = line.split()
        name = subject[0]
        proceeds = float(subject[2])
        costs = float(subject [3])
        profit = proceeds - costs
        if profit > 0:
            average_profit += profit
            count += 1
        dictionary_prof[name] = int(profit)
    dictionary['average_profit'] = int(average_profit / count)
final_list = [dictionary_prof, dictionary]
print(final_list)

with open("text_77.json", "w") as write_f:
    json.dump(final_list, write_f)


